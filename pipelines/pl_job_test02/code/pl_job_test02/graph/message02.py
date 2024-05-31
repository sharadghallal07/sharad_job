from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from pl_job_test02.config.ConfigStore import *
from pl_job_test02.udfs.UDFs import *

def message02(spark: SparkSession) -> DataFrame:
    out0 = spark.createDataFrame([("hello prophecy developer", )], ["message"])

    return out0
