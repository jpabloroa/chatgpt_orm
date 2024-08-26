import openai
from typing import List
from .model.model import Model


class Chat:

    def __init__(self, api_key=None, model="gpt-3.5-turbo"):
        self.api_key = api_key
        self.model = model
        self.previous_context = []

        if api_key:
            self.configure_auth(api_key)

    def configure_auth(self, api_key) -> None:
        """Set the API key for OpenAI."""
        self.api_key = api_key
        openai.api_key = self.api_key

    def set_model(self, model) -> None:
        """Set the model to be used in the OpenAI API request."""
        self.model = model

    def add_context(self, context) -> None:
        """Add previous context to be included in the conversation."""
        self.previous_context.append({"role": "system", "content": context})

    data_models: List[Model]

    def get_models(self) -> List[Model]:
        """Get model registered data models."""
        return self.data_models

    def set_entities(self, data_models: List[Model]) -> None:
        """Register data models."""
        self.data_models = data_models
        
    def add_role_context(self)->None:
        """Add the role context to the request."""
        # TODO
        self.add_context('You are the data manager on the following model, ')

    def make_request(self, prompt, **kwargs):
        """Make a request to the OpenAI API, including any previous context."""
        if not self.api_key:
            raise ValueError("API key is not configured.")

        messages = self.previous_context + [{"role": "user", "content": prompt}]

        response = openai.ChatCompletion.create(
            model=self.model, messages=messages, **kwargs
        )
        return response

    def new_query(self, message: str) -> str:
        return
