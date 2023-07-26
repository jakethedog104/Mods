from functools import wraps
import services
import sims4.resources
from sims4.tuning.instance_manager import InstanceManager
from sims4.resources import Types

def inject(target_function, new_function):
    @wraps(target_function)
    def _inject(*args, **kwargs):
        return new_function(target_function, *args, **kwargs)
    return _inject

def inject_to(target_object, target_function_name):
    def _inject_to(new_function):
        target_function = getattr(target_object, target_function_name)
        setattr(target_object, target_function_name, inject(target_function, new_function))
        return new_function
    return _inject_to

awingedllama_Sims3CostumeChest_ObjectIds_1 = (12513000122497208666,)
awingedllama_Sims3CostumeChest_InteractionIds_1 = (13635793276270616722,)
@inject_to(InstanceManager, 'load_data_into_class_instances')
def awingedllama_Sims3CostumeChest_AddSuperAffordances_1(original, self):
    original(self)
    if self.TYPE == Types.OBJECT:
        affordance_manager = services.affordance_manager()
        sa_list = []
        for sa_id in awingedllama_Sims3CostumeChest_InteractionIds_1:
            key = sims4.resources.get_resource_key(sa_id, Types.INTERACTION)
            sa_tuning = affordance_manager.get(key)
            if not sa_tuning is None:
                sa_list.append(sa_tuning)
        sa_tuple = tuple(sa_list)
        for obj_id in awingedllama_Sims3CostumeChest_ObjectIds_1:
            key = sims4.resources.get_resource_key(obj_id, Types.OBJECT)
            obj_tuning = self._tuned_classes.get(key)
            if not obj_tuning is None:
                obj_tuning._super_affordances = obj_tuning._super_affordances + sa_tuple
awingedllama_Sims3CostumeChest_ObjectIds_2 = (14965,)
awingedllama_Sims3CostumeChest_InteractionIds_2 = (17386139357171014384,)
@inject_to(InstanceManager, 'load_data_into_class_instances')
def awingedllama_Sims3CostumeChest_AddSuperAffordances_2(original, self):
    original(self)
    if self.TYPE == Types.OBJECT:
        affordance_manager = services.affordance_manager()
        sa_list = []
        for sa_id in awingedllama_Sims3CostumeChest_InteractionIds_2:
            key = sims4.resources.get_resource_key(sa_id, Types.INTERACTION)
            sa_tuning = affordance_manager.get(key)
            if not sa_tuning is None:
                sa_list.append(sa_tuning)
        sa_tuple = tuple(sa_list)
        for obj_id in awingedllama_Sims3CostumeChest_ObjectIds_2:
            key = sims4.resources.get_resource_key(obj_id, Types.OBJECT)
            obj_tuning = self._tuned_classes.get(key)
            if not obj_tuning is None:
                obj_tuning._super_affordances = obj_tuning._super_affordances + sa_tuple

awingedllama_Sims3CostumeChest_163702_SnippetId = 163702
awingedllama_Sims3CostumeChest_163702_MixerId = (17796672326363038924,)
@inject_to(InstanceManager, 'load_data_into_class_instances')
def awingedllama_Sims3CostumeChest_AddMixer_163702(original, self):
    original(self)
    if self.TYPE == Types.SNIPPET:
        key = sims4.resources.get_resource_key(awingedllama_Sims3CostumeChest_163702_SnippetId, Types.SNIPPET)
        snippet_tuning = self._tuned_classes.get(key)
        if snippet_tuning is None:
            return
        for m_id in awingedllama_Sims3CostumeChest_163702_MixerId:
            affordance_manager = services.affordance_manager()
            key = sims4.resources.get_resource_key(m_id, Types.INTERACTION)
            mixer_tuning = affordance_manager.get(key)
            if mixer_tuning is None:
                return
            if mixer_tuning in snippet_tuning.value:
                return
            snippet_tuning.value = snippet_tuning.value + (mixer_tuning, )

