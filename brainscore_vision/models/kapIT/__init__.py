from brainscore_vision import model_registry
from brainscore_vision.model_helpers.brain_transformation import ModelCommitment
from .model import get_model, get_layers

model_registry['kapIT'] = lambda: ModelCommitment(identifier='kapIT', activations_model=get_model('kapIT'), layers=get_layers('kapIT'))