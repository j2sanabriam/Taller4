from pydantic import BaseModel

class DataModel(BaseModel):
    SeniorCitizen: int
    TotalCharges: float
    gender: str
    Partner: str
    Dependents: str
    PhoneService: str
    MultipleLines: str
    InternetService: str
    OnlineSecurity: str
    OnlineBackup: str
    DeviceProtection: str
    TechSupport: str
    StreamingTV: str
    StreamingMovies: str
    Contract: str
    PaperlessBilling: str
    PaymentMethod: str

"""
    Tasa_de_Interes: float
    Plazo_OK: str
    Cliente: str
    Producto_Destinacion_OK: str
    Canal_de_Captura_OK: str
    Tipo_de_Empresa: str
    Ano_de_Constitucion: int
    Actividad_eco_SEMPLI: str
    Ciudad_agrupada: str
    Estrato: int
    Acceso_a_la_banca: str
    Mujeres_Empresarias: str
    Tipo_de_Garantia: str

    features = ['SeniorCitizen', 'TotalCharges', 'gender', 'Partner', 'Dependents', 'PhoneService', 'MultipleLines',
                'InternetService', 'OnlineSecurity', 'OnlineBackup',
                'DeviceProtection', 'TechSupport', 'StreamingTV', 'StreamingMovies', 'Contract', 'PaperlessBilling',
                'PaymentMethod']
"""
