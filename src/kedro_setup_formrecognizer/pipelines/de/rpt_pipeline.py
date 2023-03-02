import inspect
import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(inspect.getsourcefile(lambda: 0))))

from kedro.pipeline import Pipeline, node
import rpt_nodes


def create_pipeline(**kwargs):
    return Pipeline(
        [
            # Lookup table
            node(
                rpt_nodes.reporting_student_improvement,
                [
                    "fea_students_grades",
                ],
                "rpt_students_grades",
                name="rpt_students_grades_nd",
                tags=["rpt", "de"],
            ),
        ]
    )
