import copernicusmarine as cm
from datetime import datetime, timedelta

# Mendapatkan tanggal saat ini
current_date = datetime.now().strftime("%Y-%m-%d")

# Menambahkan 3 hari ke tanggal saat ini
end_date = (datetime.now() + timedelta(days=3)).strftime("%Y-%m-%d")


cm.subset(
  dataset_id="cmems_mod_glo_phy-so_anfc_0.083deg_P1D-m",
  dataset_version="202211",
  variables=["so"],
  minimum_longitude=108,
  maximum_longitude=111,
  minimum_latitude=-7,
  maximum_latitude=-3.5,
  start_datetime=current_date + "T00:00:00",
  end_datetime=end_date + "T00:00:00",
  minimum_depth=0.49402499198913574,
  maximum_depth=0.49402499198913574,
)