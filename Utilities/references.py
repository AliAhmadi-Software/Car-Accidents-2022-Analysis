import json
import pandas as pd


def extract_refs(ref_path):
    ref_df = pd.read_excel(ref_path)\
        .drop(columns=['table', 'field name', 'note', 'code/format'])

    casualty_class_df = ref_df.iloc[1622:1625]\
        .reset_index().drop(columns=['index'])
    casualty_class_ref = casualty_class_df.iloc[:, 0].tolist()

    casualty_gender_df = ref_df.iloc[1625:1629].reset_index()\
        .drop(columns=['index'])
    casualty_gender_ref = casualty_gender_df.iloc[:, 0].tolist()

    casualty_age_band_df = ref_df.iloc[1631:1643].reset_index()\
        .drop(columns=['index'])
    casualty_age_band_ref = casualty_age_band_df.iloc[:, 0].tolist()

    casualty_severity_df = ref_df.iloc[1643:1646].reset_index()\
        .drop(columns=['index'])
    casualty_severity_ref = casualty_severity_df.iloc[:, 0].tolist()

    pedestarian_loc_df = ref_df.iloc[1646:1658].reset_index()\
        .drop(columns=['index'])
    pedestarian_loc_ref = pedestarian_loc_df.iloc[:, 0].tolist()

    pedestarian_movement_df = ref_df.iloc[1658:1669].reset_index()\
        .drop(columns=['index'])
    pedestarian_movement_ref = pedestarian_movement_df.iloc[:, 0].tolist()

    passenger_position_df = ref_df.iloc[1669:1674].reset_index()\
        .drop(columns=['index'])
    passenger_position_ref = passenger_position_df.iloc[:, 0].tolist()

    passenger_buscoach_df = ref_df.iloc[1674:1681].reset_index()\
        .drop(columns=['index'])
    passenger_buscoach_ref = passenger_buscoach_df.iloc[:, 0].tolist()

    pedestarian_maintenance_worker_df = ref_df.iloc[1681:1686].reset_index()\
        .drop(columns=['index'])
    pedestarian_maintenance_worker_ref = pedestarian_maintenance_worker_df.iloc[:, 0].tolist()

    casualty_imd_decile_df = ref_df.iloc[1717:1728].reset_index()\
        .drop(columns=['index'])
    casualty_imd_deciel_ref = casualty_imd_decile_df.iloc[:, 0].tolist()

    casualty_area_type_df = ref_df.iloc[1728:1732].reset_index()\
        .drop(columns=['index'])
    casualty_area_type_ref = casualty_area_type_df.iloc[:, 0].tolist()

    vehicle_type_df = ref_df.iloc[1383:1413].reset_index()\
        .drop(columns=['index'])
    vehicle_type_ref = vehicle_type_df.iloc[:, 0].tolist()

    references = {
        'casualty': {
            'class': casualty_class_ref,
            'gender': casualty_gender_ref,
            'age_band': casualty_age_band_ref,
            'severity': casualty_severity_ref,
            'area_type': casualty_area_type_ref,
            'imd_decile': casualty_imd_deciel_ref,
        },
        'pedestrian': {
            'location': pedestarian_loc_ref,
            'movement': pedestarian_movement_ref,
            'maintenance_worker': pedestarian_maintenance_worker_ref,
        },
        'passenger': {
            'position': passenger_position_ref,
            'buscoach': passenger_buscoach_ref,
        },
        'vehicle': {
            'vehicle_type': vehicle_type_ref,
        }
    }

    with open('./data/references/references.json', 'w') as f:
        json.dump(references, f)


def read_refs(ref_path):
    with open(ref_path, 'r') as f:
        references = json.load(f)
    return references
