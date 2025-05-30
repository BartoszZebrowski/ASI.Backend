"""
This is a boilerplate pipeline 'data_science'
generated using Kedro 0.19.13
"""

from kedro.pipeline import node, Pipeline, pipeline  # noqa

from .nodes import evaluate_model, split_data, train_model, scale_data, one_hot_encoding


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline(
        [

            node(
                func=scale_data,
                inputs=["model_input_data"],
                outputs=["scaled_data","scaler"],
                name="scale_data_node",
            ),
            node(
                func=one_hot_encoding,
                inputs="scaled_data",
                outputs=["prepered_data","encoder"],
                name="one_hot_encoding_node",
            ),
            node(
                func=split_data,
                inputs="prepered_data",
                outputs=["X_train", "X_test", "y_train", "y_test"],
                name="split_data_node",
            ),
            node(
                func=train_model,
                inputs=["X_train", "y_train"],
                outputs="model",
                name="train_model_node",
            ),
            node(
                func=evaluate_model,
                inputs=["model", "X_test", "y_test"],
                outputs=None,
                name="evaluate_model_node",
            ),
        ]
    )
