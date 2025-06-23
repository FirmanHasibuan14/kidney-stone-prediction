import joblib
import pandas as pd
from schemas.predict import PredictionRequest

class MLService:
    def __init__(self, model_path: str):
        self.model = joblib.load(model_path)
    
        self.features = ['gravity', 'ph', 'osmo', 'cond', 'urea', 'calc', 
                         'urine_volume', 'specific_gravity_calcium_ratio', 
                         'calcium_conductivity_ratio', 'calcium_pH_interaction', 
                         'urea_pH_interaction', 'osmolarity_calcium_interaction'
                        ]
        
    def _preprocess(self, df: pd.DataFrame) -> pd.DataFrame:
        df_copy = df.copy()
        df_copy['urine_volume'] = (1000 * df_copy['gravity'] * df_copy['osmo']) / (18 * 1.001)
        df_copy['specific_gravity_calcium_ratio'] = df_copy['gravity'] / df_copy['calc']
        df_copy['calcium_conductivity_ratio'] = df_copy['calc'] / df_copy['cond']
        df_copy['calcium_pH_interaction'] = df_copy['calc'] * df_copy['ph']
        df_copy['urea_pH_interaction'] = df_copy['urea'] * df_copy['ph']
        df_copy['osmolarity_calcium_interaction'] = df_copy['osmo'] * df_copy['calc']

        return df_copy
    
    def predict(self, request_data: PredictionRequest):
        input_data = pd.DataFrame([request_data.dict()])
        processed_data = self._preprocess(input_data)  

        processed_data = processed_data[self.features]

        prediction = self.model.predict(processed_data)[0]
        probability = self.model.predict_proba(processed_data)[0][1]

        return {
            "prediction": int(prediction),
            "probability": float(probability),
            "engineered_features": processed_data.to_dict(orient='records')[0]
        }
    
ml_service = MLService(model_path="/ML/Model/kidney_stone_xgb.pkl")
