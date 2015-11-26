import psutil
from flask_restful import Resource


class Memory(Resource):
    def get(self):

        v_mem_stats = psutil.virtual_memory()
        virtual = dict(
            total=v_mem_stats[0],
            available=v_mem_stats[1],
            percent=v_mem_stats[2],
            used=v_mem_stats[3],
            free=v_mem_stats[4],
            active=v_mem_stats[5],
            inactive=v_mem_stats[6],
            buffers=v_mem_stats[7],
            cached=v_mem_stats[8]
        )

        s_mem_stats = psutil.swap_memory()
        swap = dict(
            total=s_mem_stats[0],
            used=s_mem_stats[0],
            free=s_mem_stats[0],
            percent=s_mem_stats[0],
            sin=s_mem_stats[0],
            sout=s_mem_stats[0]
        )

        return dict(
            virtual_memory_stats=virtual,
            swap_memory_stats=swap)
