"""Project pipelines."""
from typing import Dict

import inspect
import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(inspect.getsourcefile(lambda: 0))))


from kedro.framework.project import find_pipelines
from kedro.pipeline import Pipeline

from pipelines.de import pri_pipeline
from pipelines.de import fea_pipeline
from pipelines.de import rpt_pipeline

def register_pipelines() -> Dict[str, Pipeline]:
    """Register the project's pipelines.

    Returns:
        A mapping from a pipeline name to a ``Pipeline`` object.
    """
 
    pri = pri_pipeline.create_pipeline()
    fea = fea_pipeline.create_pipeline()
    rpt = rpt_pipeline.create_pipeline()
    
  
    return {
        ## Pipelines for VMX 1.5
        "de": pri + fea + rpt,
        "primary": pri,
        "feature": fea,
        "rpt": rpt,
        "__default__": pri + fea + rpt,
    }
