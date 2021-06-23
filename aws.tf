provider "aws" {
  region                  = "ap-south-1"
  profile                 = "default"
}


resource "aws_instance" "modelos1" {
	ami           = "ami-0ad704c126371a549"
	instance_type = "t2.micro"
	tags = {
		  "Name" = "My OS"
	  }
}

output "modelos1" {
  value = aws_instance.modelos1.availability_zone
}


resource "aws_ebs_volume" "vol" {
   availability_zone = aws_instance.modelos1.availability_zone 
   size              =  5

  tags = {
    Name = "my storage"
  }
}

resource "aws_volume_attachment" "ebs_att" {
  device_name = "/dev/sdh"
  volume_id   = aws_ebs_volume.vol.id
  instance_id = aws_instance.modelos1.id
}