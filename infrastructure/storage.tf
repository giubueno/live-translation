resource "aws_elasticache_serverless_cache" "api" {
    engine      = "redis"
    name        = "api"
    description = "API cache"
    cache_usage_limits {
        data_storage {
        maximum = 1
        unit    = "GB"
        }
        ecpu_per_second {
        maximum = 2000
        }
    }
    # major_engine_version = "1.6"
    security_group_ids   = [aws_security_group.elasticache.id]
    subnet_ids           = aws_subnet.main[*].id
}

resource "aws_security_group" "elasticache" {
    name        = "elasticache"
    description = "API ElastiCache security group"
    vpc_id      = aws_vpc.main.id
}