import copernicusmarine as cm
from datetime import datetime, timedelta

# Mendapatkan tanggal saat ini
current_date = datetime.now().strftime("%Y-%m-%d")

# Menambahkan 3 hari ke tanggal saat ini
end_date = (datetime.now() + timedelta(days=3)).strftime("%Y-%m-%d")


cm.subset(
  dataset_id="cmems_mod_glo_bgc-bio_anfc_0.25deg_P1D-m",
  dataset_version="202311",
  variables=["nppv"],
  minimum_longitude=108,
  maximum_longitude=111,
  minimum_latitude=-7,
  maximum_latitude=-3.5,
  start_datetime=current_date + "T00:00:00",
  end_datetime=end_date + "T00:00:00",
  minimum_depth=0.4940253794193268,
  maximum_depth=0.4940253794193268,
)
