from comfy import model_management

class ModelUnloader:
    def __init__(self):
        pass
    
    @classmethod
    def INPUT_TYPES(s):
         return {
            "required": {			
            },
        }

    RETURN_TYPES = ()
    RETURN_NAMES = ()

    FUNCTION = "unload_model"

    OUTPUT_NODE = True

    CATEGORY = "LJRE/utils"

    def unload_model(self):
        loadedmodels=model_management.current_loaded_models
        unloaded_model = False
        for i in range(len(loadedmodels) -1, -1, -1):
            m = loadedmodels.pop(i)
            m.model_unload()
            del m
            unloaded_model = True
        if unloaded_model:
            model_management.soft_empty_cache()
        return ()
