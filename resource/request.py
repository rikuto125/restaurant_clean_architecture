# resource/request.py

from pydantic import BaseModel

"""
BaseModelをrequestで使用している理由はFastAPI
においてはrequestのbodyに対してvalidationを行うため
今回におけるvalidationはdish_nameが必須であること
"""


class OrderRequest(BaseModel):
    dish_name: str
