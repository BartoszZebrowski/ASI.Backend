"""
This is a boilerplate pipeline 'data_processing'
generated using Kedro 0.19.13
"""

from kedro.pipeline import node, Pipeline, pipeline  # noqa

from .nodes import drop_columns, feature_engineering


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
        node(
            func=drop_columns,
            inputs="hr_dataset",
            outputs="hr_dataset_without_useless_columns",
            name="delete_useless_columns_node",
        ),
        
        node(
            func=feature_engineering,
            inputs="hr_dataset_without_useless_columns",
            outputs="model_input_data",
            name="feature_engineering_node",
        ),
    ])
