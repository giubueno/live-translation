resource "aws_cloudwatch_log_group" "api" {
  name = "api"

  tags = {
    Environment = "production"
    Application = "api"
  }
}