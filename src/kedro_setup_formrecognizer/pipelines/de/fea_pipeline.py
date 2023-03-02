import inspect
import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(inspect.getsourcefile(lambda: 0))))

from kedro.pipeline import Pipeline, node
import fea_nodes


def create_pipeline(**kwargs):
    return Pipeline(
        [
            # Lookup table
            node(
                fea_nodes.fe_student_improvement,
                [
                    "pri_students_grades",
                ],
                "fea_students_grades",
                name="fea_students_grades_nd",
                tags=["fea", "de"],
            ),
        ]
    )
