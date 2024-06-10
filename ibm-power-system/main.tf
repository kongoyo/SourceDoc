provider "ibm" {
  ibmcloud_api_key = "YOUR_IBM_CLOUD_API_KEY"
}

resource "ibm_pi_instance" "power_instance" {
  pi_workspace_id    = "YOUR_WORKSPACE_ID"
  pi_instance_name   = "my-power-instance"
  pi_cloud_instance_id = "YOUR_CLOUD_INSTANCE_ID"
  pi_sys_type        = "s922" # 或其他支持的系统类型
  pi_proc_type       = "dedicated" # 或"shared"
  pi_sys_count       = 1
  pi_mem             = 32 # 内存大小，单位是GB
  pi_procs           = 2  # 处理器数量
  pi_network_id      = "YOUR_NETWORK_ID"
  pi_image_id        = "YOUR_IMAGE_ID"
  pi_storage_pool    = "YOUR_STORAGE_POOL"
  pi_storage_type    = "tier3" # 或其他存储类型
  pi_storage_size    = 100 # 存储大小，单位是GB
}

