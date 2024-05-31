from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from pl_job_test02.config.ConfigStore import *
from pl_job_test02.udfs.UDFs import *
from prophecy.utils import *
from pl_job_test02.graph import *

def pipeline(spark: SparkSession) -> None:
    df_message02 = message02(spark)

def main():
    spark = SparkSession.builder\
                .config("spark.default.parallelism", "4")\
                .config("spark.sql.legacy.allowUntypedScalaUDF", "true")\
                .enableHiveSupport()\
                .appName("pl_job_test02")\
                .getOrCreate()
    Utils.initializeFromArgs(spark, parse_args())
    spark.conf.set("prophecy.metadata.pipeline.uri", "pipelines/pl_job_test02")
    registerUDFs(spark)
    
    MetricsCollector.instrument(spark = spark, pipelineId = "pipelines/pl_job_test02", config = Config)(pipeline)

if __name__ == "__main__":
    main()
