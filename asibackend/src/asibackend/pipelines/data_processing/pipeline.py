"""
This is a boilerplate pipeline 'data_processing'
generated using Kedro 0.19.13
"""

from kedro.pipeline import node, Pipeline, pipeline  # noqa

from .nodes import drop_columns


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([

        node(
            func=drop_columns,
            inputs="hr_dataset",
            outputs="preprocessed_companies",
            name="preprocess_companies_node",
        ),
    ##node(
            
            ## drop columns
            ## delate duplications ?
            ## hot encoding ?
            ## 


        ## )


    ])
