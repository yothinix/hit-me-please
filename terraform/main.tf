provider "google" {
  credentials = "${file("hitmebaby.json")}"
  project     = "hitme-242409"
  region      = "asia-southeast1"
  zone        = "asia-southeast1-b"
}
