variable "sendgrid_api_key" {
  description = "SendGrid API key"
  type        = string
  sensitive   = true
  default     = "placeholder"
}

variable "SETUP_JOB_PASSWORD" {
  description = "This is the first vendor password"
  type        = string
  sensitive   = true
}

variable "TWILIO_TOKEN" {
  description = "Twilio token"
  type        = string
  sensitive   = true
  default     = "placeholder"
}

variable "TWILIO_ACCOUNTID" {
  description = "Twilio account ID"
  type        = string
  sensitive   = true
  default     = "placeholder"
}