from wq.db import rest
from .models import Consumer


rest.router.register_model(
    Consumer,
    fields="__all__",
)
