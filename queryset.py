

from viewser.models import Queryset, DatabaseOperation, TransformOperation, RenameOperation
from viewser.operations import publish, fetch

queryset = Queryset(
            name =  "conflict_history_queryset",
            themes = ["conflict history"],
            description = """
                This is a simple queryset for testing conflict history models.
            """,
            loa = "country_month",
            operations = [
                    [
                        RenameOperation(arguments = ["ged_lag_3"]),
                        TransformOperation(name = "temporal.tlag",arguments=["3"]),
                        TransformOperation(name = "ops.gte",arguments=["25"]),
                        DatabaseOperation(name = "priogrid_month.ged_best_ns",arguments=["sum"]),
                    ],
                    [
                        RenameOperation(arguments = ["ged_lag_2"]),
                        TransformOperation(name = "temporal.tlag",arguments=["2"]),
                        TransformOperation(name = "ops.gte",arguments=["25"]),
                        DatabaseOperation(name = "priogrid_month.ged_best_ns",arguments=["sum"]),
                    ],
                    [
                        RenameOperation(arguments = ["ged_lag_1"]),
                        TransformOperation(name = "temporal.tlag",arguments=["1"]),
                        TransformOperation(name = "ops.gte",arguments=["25"]),
                        DatabaseOperation(name = "priogrid_month.ged_best_ns",arguments=["sum"]),
                    ],
                    [
                        RenameOperation(arguments = ["ged_decay"]),
                        TransformOperation(name = "temporal.decay",arguments=["12"]),
                        TransformOperation(name = "temporal.time_since",arguments=["0","0"]),
                        TransformOperation(name = "ops.gte",arguments=["25"]),
                        DatabaseOperation(name = "priogrid_month.ged_best_ns",arguments=["sum"]),
                    ],
                    [
                        RenameOperation(arguments = ["ged"]),
                        TransformOperation(name = "ops.gte",arguments=["25"]),
                        DatabaseOperation(name = "priogrid_month.ged_best_ns",arguments=["sum"]),
                    ]
                ]

        )

publish(queryset)
fetch(queryset.name).to_parquet("data.parquet")
