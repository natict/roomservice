import psutil
from flask_restful import Resource


class Memory(Resource):
    def get(self):

        v_mem_stats = psutil.virtual_memory()
        virtual = {}
        for k, v in vars(v_mem_stats).items():
            virtual.update({k: v})

        s_mem_stats = psutil.swap_memory()
        swap = {}
        for k, v in vars(s_mem_stats).items():
            swap.update({k: v})

        return dict(
            virtual_memory_stats=virtual,
            swap_memory_stats=swap)
