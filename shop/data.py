from dataclasses import dataclass
from unicodedata import name

@dataclass
class ArticleInTemplate:
  pk : int 
  name: str 
  price: float 
  description: str 
  is_send : bool 
  category: str 
  image : str 
  city : str
  user : str
  image_article_count: int
  