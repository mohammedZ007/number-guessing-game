output "instance_public_ip" {
  description = "Public IP address of the CD server"
  value       = aws_instance.cd_server.public_ip
}

output "instance_public_dns" {
  description = "Public DNS name of the CD server"
  value       = aws_instance.cd_server.public_dns
}
