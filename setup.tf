variable "aws_region" {
  type = string
}

variable "aws_accesskey" {
  type = string
}

variable "aws_secretkey" {
  type = string
}

variable "bucket_name" {
  type = string
}

provider "aws" {
  region     = var.aws_region
  access_key = var.aws_accesskey
  secret_key = var.aws_secretkey
}

resource "aws_s3_bucket" "tdc-bucket" {
  bucket = var.bucket_name
  acl    = "private"
}

