import numpy as np
from pyarrow import dataset as ds
import pandas
import numpy as np
from pyarrow import compute as pc
import math 
import sys
sys.path.insert(0,'/global/cfs/projectdirs/lsst/groups/SRV/gcr-catalogs-test')
import GCRCatalogs


def convert_nanoJansky_to_mag(flux):
    """Convert calibrated nanoJansky flux to AB mag.
    """
    AB_mag_zp_wrt_Jansky = 8.90  # Definition of AB
    # 9 is from nano=10**(-9)
    AB_mag_zp_wrt_nanoJansky = 2.5 * 9 + AB_mag_zp_wrt_Jansky

    return -2.5 * np.log10(flux) + AB_mag_zp_wrt_nanoJansky

def convert_flux_err_to_mag_err(flux, flux_err):
    """Convert flux and flux err to mag err.

    Assumes flux_err is symmetric.
    Uses instantaneous derivative.
    So a negative flux measurement (with a positive flux_err) will produce a finite, but negative mag_err.
    """
    return (2.5 / math.log(10)) * (flux_err / flux)


def e(ixx,ixy,iyy):
    ixx = np.complex128(ixx)
    ixy = np.complex128(ixy)
    iyy = np.complex128(iyy)
    denom = (ixx+iyy + 2.*np.sqrt(ixx*iyy-ixy**2))
    e = (ixx-iyy+2*ixy*1j)/denom
    return e


def get_matched_catalog():
    path_object='/global/cfs/cdirs/lsst/shared/rubin/DP0.2/objectTable/objectTable_tract_4850_DC2_2_2i_runs_DP0_2_v23_0_1_PREOPS-905_step3_27_20220316T171018Z.parq'
    path_truth = '/global/cfs/projectdirs/lsst/shared/DC2-prod/Run2.2i/truth/truth_merged_summary_v1-0-0/raw/truth_tract4850.parquet'
    path_truth_match = '/global/cfs/projectdirs/lsst/shared/rubin/DP0.2/match_ref_truth_summary_objectTable/match_ref_truth_summary_objectTable_tract_4850_DC2_u_ctslater_matchObjectToTruth_w22_20220527T164747Z.parq'


    dataset = ds.dataset(path_object)
    truth = ds.dataset(path_truth) 
    match = ds.dataset(path_truth_match)
    
    truth_pandas = truth.to_table().to_pandas(ignore_metadata=True)
    match_pandas = match.to_table().to_pandas(ignore_metadata=True)

    truth_match_dataset = match.join(
        truth.filter(pc.field("truth_type")==1
                    ),
        "id",
        right_keys="id_string",
        join_type="inner",
        left_suffix="_match",
        right_suffix="_truth",
    )
    
    truth_match_dataset = match.join(
        truth.filter(
            pc.field("truth_type") == 1
        ),
        "id",
        right_keys="id_string",
        join_type="inner",
        left_suffix="_match",
        right_suffix="_truth",
    )
    object_match_dataset = dataset.filter(
        pc.field("detect_isPrimary") & (pc.field("refExtendedness") == 1)
    ).join(
        truth_match_dataset,
        "objectId",
        right_keys="match_objectId",
        join_type="inner",
        left_suffix="_object",
    )
    object_match_dataset = object_match_dataset.to_table().to_pandas()
    match_pandas['id_str'] = match_pandas['id'].astype('str')
    truth_gals = truth_pandas[truth_pandas['truth_type']==1]
    
    
    catalog = 'lsst_object'
    catalog_instance =  GCRCatalogs.load_catalog(catalog)   
    sources = [parquet_data.path for parquet_data in catalog_instance._datasets]
    dataset = ds.dataset(sources)
    dataset = dataset.to_table().to_pandas(ignore_metadata=True) # otherwise it'll suppress objectID 
    # let's do a merge - this requires objectID to be unique, but multiple object IDs can match to the same truth object
    matched_table = pandas.merge(truth_gals,match_pandas,how='inner',left_on='id_string', right_on='id_str', sort=False, suffixes=('_truth','_match'),validate='one_to_many')
    matched_table = pandas.merge(dataset,matched_table,how='inner',left_on='objectId', right_on='match_objectId', sort=False, suffixes=('_object',''),validate='one_to_many')
    return matched_table

def get_matched_catalog_stars():
    path_object='/global/cfs/cdirs/lsst/shared/rubin/DP0.2/objectTable/objectTable_tract_4850_DC2_2_2i_runs_DP0_2_v23_0_1_PREOPS-905_step3_27_20220316T171018Z.parq'
    path_truth = '/global/cfs/projectdirs/lsst/shared/DC2-prod/Run2.2i/truth/truth_merged_summary_v1-0-0/raw/truth_tract4850.parquet'
    path_truth_match = '/global/cfs/projectdirs/lsst/shared/rubin/DP0.2/match_ref_truth_summary_objectTable/match_ref_truth_summary_objectTable_tract_4850_DC2_u_ctslater_matchObjectToTruth_w22_20220527T164747Z.parq'


    dataset = ds.dataset(path_object)
    truth = ds.dataset(path_truth) 
    match = ds.dataset(path_truth_match)
    
    truth_pandas = truth.to_table().to_pandas(ignore_metadata=True)
    match_pandas = match.to_table().to_pandas(ignore_metadata=True)

    truth_match_dataset = match.join(
        truth.filter(pc.field("truth_type")==1
                    ),
        "id",
        right_keys="id_string",
        join_type="inner",
        left_suffix="_match",
        right_suffix="_truth",
    )
    
    truth_match_dataset = match.join(
        truth.filter(
            pc.field("truth_type") == 2
        ),
        "id",
        right_keys="id_string",
        join_type="inner",
        left_suffix="_match",
        right_suffix="_truth",
    )
    object_match_dataset = dataset.filter(
        pc.field("detect_isPrimary") & (pc.field("refExtendedness") == 0)
    ).join(
        truth_match_dataset,
        "objectId",
        right_keys="match_objectId",
        join_type="inner",
        left_suffix="_object",
    )
    object_match_dataset = object_match_dataset.to_table().to_pandas()
    match_pandas['id_str'] = match_pandas['id'].astype('str')
    truth_gals = truth_pandas[truth_pandas['truth_type']==2]
    
    
    catalog = 'lsst_object'
    catalog_instance =  GCRCatalogs.load_catalog(catalog)   
    sources = [parquet_data.path for parquet_data in catalog_instance._datasets]
    dataset = ds.dataset(sources)
    dataset = dataset.to_table().to_pandas(ignore_metadata=True) # otherwise it'll suppress objectID 
    # let's do a merge - this requires objectID to be unique, but multiple object IDs can match to the same truth object
    matched_table = pandas.merge(truth_gals,match_pandas,how='inner',left_on='id_string', right_on='id_str', sort=False, suffixes=('_truth','_match'),validate='one_to_many')
    matched_table = pandas.merge(dataset,matched_table,how='inner',left_on='objectId', right_on='match_objectId', sort=False, suffixes=('_object',''),validate='one_to_many')
    return matched_table