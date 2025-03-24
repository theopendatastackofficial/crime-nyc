from dagster import AssetExecutionContext, asset, AssetIn, MetadataValue
from dagster_dbt import DbtCliResource, dbt_assets, DagsterDbtTranslator
from dagster_dbt import DbtProject
from pathlib import Path
from typing import Any, Mapping, Optional

# Get the root of the project (two levels up from this script)
ROOT_DIR = Path(__file__).parent.parent.parent.resolve()

# Set the path to MTA's DBT project folder
dbt_project = DbtProject(
    project_dir=ROOT_DIR.joinpath("transformations", "dbt"),  # The DBT project is in your_project_root/transformations/dbt
)

# Define a custom DagsterDbtTranslator
class CustomDagsterDbtTranslator(DagsterDbtTranslator):
    def get_metadata(self, dbt_resource_props: Mapping[str, Any]) -> Mapping[str, Any]:
        # Customize the metadata extraction logic
        return {
            "dbt_metadata": MetadataValue.json(dbt_resource_props.get("meta", {}))
        }

    def get_group_name(self, dbt_resource_props: Mapping[str, Any]) -> Optional[str]:
        # Map dbt folders to Dagster groups
        return dbt_resource_props.get("folder", "DBT_Transformations")

# Use the custom translator in your dbt_assets definition
@dbt_assets(
    manifest=dbt_project.manifest_path,
    dagster_dbt_translator=CustomDagsterDbtTranslator()
)
def dbt_project_assets(context: AssetExecutionContext, dbt: DbtCliResource):
    yield from dbt.cli(["build"], context=context).stream()

