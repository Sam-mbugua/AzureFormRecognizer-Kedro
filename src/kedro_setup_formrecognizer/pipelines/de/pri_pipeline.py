import inspect
import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(inspect.getsourcefile(lambda: 0))))

from kedro.pipeline import Pipeline, node
import pri_nodes


def create_pipeline(**kwargs):
    return Pipeline(
        [
            # Lookup table
            node(
                pri_nodes.pri_clean_student_perf,
                [
                    "raw_students_grades",
                ],
                "pri_students_grades",
                name="pri_students_grades_nd",
                tags=["pri", "de"],
            ),
        ]
    )
