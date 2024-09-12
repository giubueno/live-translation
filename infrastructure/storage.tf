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

resource "aws_vpc_security_group_ingress_rule" "allow_elasticache_ipv4" {
    security_group_id = aws_security_group.elasticache.id
    cidr_ipv4         = aws_vpc.main.cidr_block
    from_port         = 6379
    ip_protocol       = "tcp"
    to_port           = 6379
}