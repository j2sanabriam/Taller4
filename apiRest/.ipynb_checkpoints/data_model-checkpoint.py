from pydantic import BaseModel

class DataModel(BaseModel):
    Valor_OK: str
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

