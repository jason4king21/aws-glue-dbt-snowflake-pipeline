from diagrams import Diagram, Node
from diagrams.aws.network import APIGateway
from diagrams.aws.compute import Lambda
from diagrams.aws.analytics import KinesisDataFirehose
from diagrams.aws.storage import S3
from diagrams.saas.analytics import Snowflake



with Diagram("Real-Time Streaming Pipeline", show=False, filename="../diagrams/architecture", outformat="png"):
    api = APIGateway("API Gateway")
    lam = Lambda("Lambda Processor")
    firehose = KinesisDataFirehose("Firehose")
    s3 = S3("S3 Bucket")
    s3error = S3("Error Logs")
    snowflake = Snowflake("Snowflake")

    api >> lam >> firehose >> s3 >> snowflake
    lam >> s3error