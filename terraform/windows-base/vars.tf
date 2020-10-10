variable "AWS_ACCESS_KEY" {
}

variable "AWS_SECRET_KEY" {
}

variable "AWS_REGION" {
  default = "us-east-1"
}

# Note: WIN_AMIS is now Replaced by ami.tf
#variable "WIN_AMIS" {
#  type = map(string)
#  default = {
#    us-east-1 = "ami-0eb7fbcc77e5e6ec6"
#  }
#}

variable "PATH_TO_PRIVATE_KEY" {
  default = "mykey2"
}

variable "PATH_TO_PUBLIC_KEY" {
  default = "mykey2.pub"
}

variable "INSTANCE_USERNAME" {
  default = "Terraform"
}

variable "INSTANCE_PASSWORD" {
}

