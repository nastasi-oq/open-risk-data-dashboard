# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-08-11 11:50
from __future__ import unicode_literals

from django.db import migrations
from django.core import serializers
from django.core.management import call_command

import json

mv_keydatasets = {"HA_9A": "BA_5", "HA_9B": "BA_6",
                  "HA_14A": "HA_23A", "HA_14B": "HA_23B",
                  "EX_7": "RI_2"}

rm_keydatasets = ["HA_19", "HA_20", "HA_22", "EX_8A", "EX_8B", "EX_7"]

new_keydatasetnames = {
    'BA_1A': 'Digital Elevation Model',
    'BA_1B': 'Digital Elevation Model',
    'BA_2A': 'Aerial Imagery',
    'BA_2B': 'Aerial Imagery',
    'BA_3': 'Administrative Boundaries',
    'BA_4': 'Topographic Map',
    'HA_1': 'Watershed Boundaries',
    'HA_2': 'Water Bodies',
    'HA_4': 'Soil Type',
    'HA_5': 'Soil Type',
    'HA_6A': 'Flood Hazard Maps',
    'HA_6B': 'Flood Hazard Maps',
    'HA_7': 'Meteorological Gauge Data',
    'HA_8': 'Hydrological Gauge Data',
    'HA_10': 'Nearshore Tsunami Wave Height',
    'HA_11A': 'Storm Surge Gauge Data',
    'HA_11B': 'Coastal Inundation',
    'HA_12': 'Flood Protection Measures',
    'HA_13': 'Cyclone Wind Speed Statistics',
    'HA_15A': 'Active Seismic Fault',
    'HA_15B': 'Active Seismic Fault',
    'HA_16A': 'Seismic Hazard Curves',
    'HA_16B': 'Seismic Hazard Map',
    'HA_17A': 'Seismic Hazard Model',
    'HA_17B': 'Seismic Hazard Model',
    'HA_18A': 'Site Conditions Map',
    'HA_18B': 'Site Conditions Map',
    'HA_21': 'List Type Of Volcanoes',
    'HA_23A': 'Hazard Scenarios',
    'HA_23B': 'Historical Records',
    'EX_1': 'Land Cover',
    'EX_2A': 'Population',
    'EX_2B': 'Population',
    'EX_3A': 'Economic Activities',
    'EX_3D': 'Company Register',
    'EX_3B': 'Economic Activities',
    'EX_4': 'Buildings',
    'EX_5': 'Agricultural Production',
    'EX_6': 'Critical Infrastructure',
    'VU_1': 'Vulnerability Curves For Aggregated Assets At'
            ' Administrative Unit Level',
    'VU_2': 'Vulnerability Curves Per Land Cover Type',
    'VU_3': 'Vulnerability Curves For Critical Infrastructure',
    'VU_4': 'Vulnerability Curves For Population',
    'VU_5A': 'Economy Vulnerability Curve',
    'VU_5B': 'Vulnerability Curves For Economic Activities',
    'VU_5C': 'Economy Vulnerability Curve',
    'VU_6': 'Vulnerability Curves For Buildings',
    'VU_7A': 'Vulnerability Curves For Agricultural Activities',
    'VU_7B': 'Agriculture Vulnerability Curve',
    'RI_1A': 'Risk Indicators From Previous Studies',
    'RI_1B': 'Risk Assessment',
    'RI_2': 'Historical Records Of Previous Natural Disasters',
}

new_keydataset_descr = {
    "BA_1A": "Digital elevation model (DEM) describing the terrain's surface"
             " with a horizontal resolution of at least 100 meters and"
             " covering all flood prone areas. The Digital elevation"
             " model includes a digital surface model (DSM) of"
             " surface elevation including objects (e.g."
             " buildings and trees) and a Digital"
             " terrain model (DTM) of the bare ground surface. ",
    "BA_1B": "Digital elevation model (DEM) describing the terrain's surface"
             " with a resolution of at least X meters and covering the"
             " whole or part of the territory. Digital elevation"
             " model includes digital terrain model (DTM)"
             " representing the bare ground of the earth"
             " as well as digital surface model (DSM)"
             " with buildings and other objects. ",
    "BA_2A": "Aerial imagery, such as vertical view or orthophoto, covering"
             " the whole territory, with a resolution of at least 10 meters.",
    "BA_2B": "Aerial imagery, such as vertical view or orthophoto, covering"
             " the whole or part of the territory, with a resolution of at"
             " least X meters.",
    "BA_3": "Shapes of official boundaries of the country and its"
            " administrative units such as states, regions, or districts. ",
    "BA_4": "Topographic map at 1:100,000 or better scale with names of main"
            " geographical places (toponyms), including cities and villages.",
    "HA_1": "Shapes of watershed boundaries for the characterization of river"
            " basins for the whole territory. Watershed boundaries are"
            " topographic divides and delineate areas where"
            " surface-water runoff drains into a common surface-water body.",
    "HA_2": "Shapes of main water bodies (river network, lakes, coastline)"
            " ",
    "HA_4": "Map of geological characterization of the soil type, with"
            " resolution of at least 1 km",
    "HA_5": "Map of geological characterization of the soil type, with"
            " resolution of at least 200 km",
    "HA_6A": "Flood hazard maps at any available resolution for benchmarking"
             " of the flood model. A flood hazard map describes the"
             " geographical areas that are prone to flooding for a"
             " given return period (typically between 2 and 1000"
             " years). Additional value is provided by maps"
             " that indicate water depth and flood duration. ",
    "HA_6B": "Flood hazard map, including water depth, duration and flow"
             " velocity, for different return periods. Flood hazard map"
             " describes wich geographical area are prone to flooding"
             " and to what extent.",
    "HA_7": "Historical gauge data of rainfall, temperature and wind. Several"
            " stations across the area of interest and daily records."
            " Sub-daily records are needed for flash flood"
            " modelling. Wind data can be used also in"
            " coastal flooding as well as volcano related computations.",
    "HA_8": "Historical water levels and river discharges from gauge stations"
            " on major river branches. Daily records and annual maxima. ",
    "HA_10": "Tsunami wave heights at nearshore locations for a range of"
             " return periods between 2 and 1000 years. ",
    "HA_11A": "Historical sea level data from coastal gauge stations. Hourly"
              " records and/or daily maxima.",
    "HA_12": "Shapes of all major flood defense structures (levees, flood"
             " walls, dams, diversions, etc) reflecting the most recent"
             " flood mitigation constructions",
    "HA_13": "Maximum wind speed (open water wind) for a range of return"
             " periods, typically between 2 and 1000 years",
    "HA_16A": "Seismic hazard curves expressing the probablity of exceeding a"
              " number of intensity measure levels within a time period"
              " (e.g. annually or in 50 years). Typically these curves"
              " are calculated considering soil type equal to rock"
              " (Vs30 = 760 m/s), and various intensity measure"
              " types (Peak Ground Acceleration or Spectral"
              " Aceleration at different periods of"
              " vibration - 0.3s and 1.0 s).",
    "HA_17A": "A probabilistic seismic hazard model describing the seismogenic"
              " sources in the country and the ground motion prediction"
              " equations that should be used. This model can be used"
              " to compute seismic hazard curves and maps.",
    "HA_17B": "A probabilistic seismic hazard model describing the seismogenic"
              " sources in the region and the ground motion prediction"
              " equations that should be used. This model can be used"
              " to compute seismic hazard curves and maps.",
    "HA_18A": "A map describing the soil conditions that can be used to"
              " calculate seismic hazard at the surface. These maps"
              " are typically part of microzonation studies, but"
              " for seismic hazard calculations in large"
              " regions geology maps can also be used. ",
    "HA_18B": "A map describing the soil conditions that can be used to"
              " calculate seismic hazard at the surface. These maps"
              " are part of microzonation studies. ",
    "HA_21": "Basic geographic and geologic information for volcanoes located"
             " in the country  including name, position, summit elevation,"
             " and volcano type.",
    "HA_23A": "Historical records of significant natural hazard events in the"
              " country including the type, intensity, footprint,"
              " description and date of the hazard events."
              " Historical records may refer to only one"
              " or more hazard types. Data may also"
              " contain non observed but plausible"
              " scenarios of hazard events.",
    "HA_23B": "Historical records of all natural hazard events in the country"
              " including at least the type, intensity, description, date"
              " and location of the hazard events. Historical records"
              " may refer to only one or more hazard types.",
    "EX_1": "Map of land cover (physical material at the surface of the earth"
            " such as grass, asphalt, trees, water) for the whole territory."
            " Land cover may also include types of land use such as urban"
            " or agriculture. Resolution must be at least 1 km. ",
    "EX_2A": "Map of population distribution, usually from census data,"
             " disagregated at the lowest administrative level"
             " (district, zipcode, block, etc.). Resolution"
             " must be at least 1 km. ",
    "EX_3A": "Statistics of economic activities for the country at the most"
             " detailed level,and  including at least the Gross Domestic"
             " Product (GDP) per economic sector.",
    "EX_3D": "List of registered companies for the country including their"
             " addresses and economic sector. ",
    "EX_4": "Map showing number and characteristics of buildings, including"
            " type of use (residential, commercial, industrial), either at"
            " the most detailed administrative unit (district, block,"
            " etc.) or, if possible, on a per-building basis.",
    "EX_5": "Map of the average annual agricultural production per acre of"
            " land, where possible subdivided per type of crop or cattle,"
            " either per smallest administrative unit or per square km. ",
    "EX_6": "Shapes of lifeline infrastructures such as utilities that provide"
            " essential services to the people. Crititical infrastructures"
            " include roads, railways, power, water, and"
            " telecommunication networks and assets as"
            " well as bridges, airports, harbors,"
            " education and health facilities.",
    "VU_1": "Functions for calculating the economic damage on all assets in a"
            " certain area from the hazard level (e.g. flood depth or"
            " earthquake intensity) ",
    "VU_2": "Functions for calculating the economic damage from hazard level"
            " (e.g. flood depth or earthquake intensity) and type of land"
            " cover",
    "VU_3": "Functions for calculating the damage on critical infrastructure"
            " from hazard level (e.g. flood depth or earthquake intensity) ",
    "VU_4": "Functions for calculating the number of people affected and"
            " fatalities from hazard level (e.g. flood depth or"
            " earthquake intensity) and population density",
    "VU_5B": "Functions for calculating the economic damage from hazard level"
             " (e.g. flood depth or earthquake intensity) and information"
             " about economic activities (e.g. GPD per economic sector)",
    "VU_6": "Functions for calculating the economic damage on buildings from"
            " hazard level (e.g. flood depth or earthquake intensity) and"
            " building type",
    "VU_7A": "Functions for calculating the economic damage on agriculture"
             " from hazard level (e.g. flood depth or earthquake"
             " intensity) and agriculture production",
    "RI_1A": "Results from previous risk assessments for comparison. These"
             " may consist of: \n-  Risk maps (gridded or aggregated"
             " per administrative unit). Risk level may indicate AAL,"
             " losses from a single event or losses for a given"
             " return period.\n-  Tabulated risk per a given"
             " area, for example Loss Exceedance Curve,"
             " Event Loss Tables, Year Loss Tables or"
             " historical loss data.\n-  Exposed"
             " assets for a given event"
             " (historical or associated with a return period). \n\n",
    "RI_2": "information about affected exposure during previous hazard"
            " events",
    }


def forwards_func(apps, schema_editor):
    # We get the model from the versioned app registry;
    # if we directly import it, it'll be the wrong version
    KeyDataset = apps.get_model("ordd_api", "KeyDataset")
    KeyCategory = apps.get_model("ordd_api", "KeyCategory")
    KeyDatasetName = apps.get_model("ordd_api", "KeyDatasetName")
    KeyTagGroup = apps.get_model("ordd_api", "KeyTagGroup")
    KeyTag = apps.get_model("ordd_api", "KeyTag")
    KeyLevel = apps.get_model("ordd_api", "KeyLevel")
    Dataset = apps.get_model("ordd_api", "Dataset")

    db_alias = schema_editor.connection.alias

    # check for contentless database
    kd_check = KeyDataset.objects.using(db_alias).all()
    if kd_check.count() == 0:
        return
    
    klevel_loc = KeyLevel.objects.using(db_alias).get(name='Local')
    klevel_nat = KeyLevel.objects.using(db_alias).get(name='National')
    klevel_int = KeyLevel.objects.using(db_alias).get(name='International')

    ktaggrp_ha = KeyTagGroup.objects.using(db_alias).get(name='hazard')

    kcat_ba = KeyCategory.objects.using(db_alias).get(code='BA')
    kcat_ha = KeyCategory.objects.using(db_alias).get(code='HA')
    kcat_ri = KeyCategory.objects.using(db_alias).get(code='RI')
    kcat_ex = KeyCategory.objects.using(db_alias).get(code='EX')

    # NEW TIME REFERENCE TAG GROUP
    ktaggrp_timeref = KeyTagGroup.objects.using(db_alias).create(
        name='time reference')

    KeyTag.objects.using(db_alias).create(
        name='Present', group=ktaggrp_timeref, is_peril=False)

    KeyTag.objects.using(db_alias).create(
        name='Future projection', group=ktaggrp_timeref,
        is_peril=False)

    # NEW BA_5
    kdname = KeyDatasetName.objects.using(db_alias).get(name='Bathymetry')
    kd = KeyDataset.objects.using(db_alias).create(
        code='BA_5', category=kcat_ba, dataset=kdname,
        tag_available=ktaggrp_ha,
        description="Bathymetry map describing the terrain that lies"
        " underwater, or the depth of water relative to sea level, with"
        " a resolution of at least 10 meters.",
        level=klevel_nat, format="raster (.tif)", comment="", weight=10)

    kd.applicability.add(KeyTag.objects.using(db_alias).get(name='Coastal '
                                                            'flooding'),
                         KeyTag.objects.using(db_alias).get(name='Tsunami'))

    # NEW BA_6
    kd = KeyDataset.objects.using(db_alias).create(
        code='BA_6', category=kcat_ba, dataset=kdname,
        tag_available=ktaggrp_ha,
        description="Bathymetry map describing the terrain that lies"
        " underwater, or the depth of water relative to sea level, with"
        " a resolution of 100 meters or higher.",
        level=klevel_nat, format="raster (.tif)", comment="", weight=10)

    kd.applicability.add(KeyTag.objects.using(db_alias).get(name='Coastal '
                                                            'flooding'),
                         KeyTag.objects.using(db_alias).get(name='Tsunami'))

    # NEW HA_23A
    kdname_scen = KeyDatasetName.objects.using(db_alias).create(
        name="Hazard scenarios")

    kd = KeyDataset.objects.using(db_alias).create(
        code='HA_23A', category=kcat_ha, dataset=kdname_scen,
        tag_available=ktaggrp_ha,
        description="Historical records of significant natural hazard"
        " events in the country including the type, intensity, footprint,"
        " description and date of the hazard events. Historical records"
        " may refer to only one or more hazard types. Data may also contain"
        " non observed but plausible scenarios of hazard events.",
        level=klevel_nat, comment="", weight=10)

    # NEW HA_23B
    kdname_rec = KeyDatasetName.objects.using(db_alias).get(
        name="Historical records")

    kd = KeyDataset.objects.using(db_alias).create(
        code='HA_23B', category=kcat_ha, dataset=kdname_rec,
        tag_available=ktaggrp_ha,
        description="Historical records of all natural hazard events in the"
        " country including at least the type, intensity, description, date"
        " and location of the hazard events. Historical records may refer"
        " to only one or more hazard types.",
        level=klevel_loc, comment="", weight=10)

    # NEW RI_2
    kdname = KeyDatasetName.objects.using(db_alias).get(
        name="records of previous natural disasters")

    kd = KeyDataset.objects.using(db_alias).create(
        code='RI_2', category=kcat_ri, dataset=kdname,
        tag_available=ktaggrp_ha,
        description="Information about affected exposure during"
        " previous hazard.",
        level=klevel_nat, comment="", weight=10)

    # NEW EX_3D
    kdname = KeyDatasetName.objects.using(db_alias).create(
        name='Company register')

    kd = KeyDataset.objects.using(db_alias).create(
        code='EX_3D', category=kcat_ex, dataset=kdname,
        tag_available=ktaggrp_timeref,
        description="List of registered companies for the country"
        " including their addresses and economic sector.",
        level=klevel_nat, comment="", weight=10)

    kd.applicability.add(*list(KeyTag.objects.using(
        db_alias).filter(is_peril=True)))

    # MOVE DATASETS BETWEEN KEYDATASETS
    for kd_code, kd_code_new in mv_keydatasets.items():
        print(kd_code)
        kd = KeyDataset.objects.using(db_alias).get(code=kd_code)
        kd_new = KeyDataset.objects.using(db_alias).get(
            code=kd_code_new)

        datasets = Dataset.objects.using(db_alias).filter(
            keydataset=kd)
        for ds in datasets:
            print(ds)
            ds.keydataset = kd_new
            ds.save()

    # REMOVE OBSOLETE KEYDATASETS
    kds = KeyDataset.objects.using(db_alias).filter(code__in=rm_keydatasets)

    print("RM COUNT: %d" % kds.count())
    data = serializers.serialize("json", kds, indent=4)
    out = open("v9_keydatasets_deleted.json", "w")
    out.write(data)
    out.close()

    kds.delete()

    # NEW DATASETNAMES
    # save previous KeyDatasetName and keydataset
    kds = KeyDataset.objects.using(db_alias).all()

    data = serializers.serialize("json", kds, indent=4)
    out = open("v9_keydatasets_pre_kdname-change.json", "w")
    out.write(data)
    out.close()

    kdsname = KeyDatasetName.objects.using(db_alias).all()
    data = serializers.serialize("json", kdsname, indent=4)
    out = open("v9_keydatasetnames_pre_kdname-change.json", "w")
    out.write(data)
    out.close()

    # CHANGE DATASETNAMES IN KEYDATASETS
    new_names = []
    # update keydataset with new keydatasetnames and create them if needed
    for code, name in new_keydatasetnames.items():
        kd = KeyDataset.objects.using(db_alias).get(code=code)
        try:
            kdname = KeyDatasetName.objects.using(db_alias).get(
                name__iexact=name)
            kdname.name = name
            kdname.category = None
            kdname.save()
            print("[%s:%s] already found" % (kdname.name, kdname.category))
        except:
            kdname = KeyDatasetName.objects.using(db_alias).create(
                name=name, category=None)
            kdname.save()
            print("[%s:%s] not found, create" % (kdname.name, kdname.category))
            new_names.append([kdname.name, kdname.category])

        kd.dataset = kdname
        kd.save()

    with open("new_keydatasetnames.json", "w") as f:
        json.dump(new_names, f)

    # delete keydatasetname without any keydataset reference
    kdnames = KeyDatasetName.objects.using(db_alias).filter(keydatasets=None)
    kdnames.delete()

    kdnames = KeyDatasetName.objects.using(db_alias).exclude(category=None)
    for kdname in kdnames:
        kdname.category = None
        kdname.save()

    for code, desc in new_keydataset_descr.items():
        kd = KeyDataset.objects.using(db_alias).get(code=code)
        kd.description = desc.strip()
        kd.save()


def backwards_func(apps, schema_editor):
    KeyDatasetName = apps.get_model("ordd_api", "KeyDatasetName")
    KeyDataset = apps.get_model("ordd_api", "KeyDataset")
    KeyTagGroup = apps.get_model("ordd_api", "KeyTagGroup")
    KeyTag = apps.get_model("ordd_api", "KeyTag")
    Dataset = apps.get_model("ordd_api", "Dataset")

    db_alias = schema_editor.connection.alias

    # check for contentless database
    kd_check = KeyDataset.objects.using(db_alias).all()
    if kd_check.count() == 0:
        return
    
    # NEW DATASETNAMES
    call_command('loaddata', 'v9_keydatasetnames_pre_kdname-change.json',
                 commit=False,
                 verbosity=0)

    call_command('loaddata', 'v9_keydatasets_pre_kdname-change.json',
                 commit=False,
                 verbosity=0)

    with open("new_keydatasetnames.json", "r") as f:
        new_names = json.load(f)

        for new_name in new_names:
            kdname = KeyDatasetName.objects.using(db_alias).get(
                name=new_name[0], category=new_name[1])
            kdname.delete()

        print("TWO")

    # REMOVE OBSOLETE KEYDATASETS
    call_command('loaddata', 'v9_keydatasets_deleted.json',
                 commit=False,
                 verbosity=0)

    # MOVE DATASETS BETWEN KEYDATASETS
    for kd_code_old, kd_code in mv_keydatasets.items():
        print(kd_code_old)
        kd = KeyDataset.objects.using(db_alias).get(code=kd_code)
        kd_old = KeyDataset.objects.using(db_alias).get(
            code=kd_code_old)

        datasets = Dataset.objects.using(db_alias).filter(
            keydataset=kd)

        for ds in datasets:
            print(ds)
            ds.keydataset = kd_old
            ds.save()

    kd = KeyDataset.objects.using(db_alias).get(code='EX_3D')
    kd.delete()

    kdname = KeyDatasetName.objects.using(db_alias).get(
        name='Company register')
    kdname.delete()

    kd = KeyDataset.objects.using(db_alias).get(code='RI_2')
    kd.delete()

    kd = KeyDataset.objects.using(db_alias).get(code='HA_23B')
    kd.delete()

    kd = KeyDataset.objects.using(db_alias).get(code='HA_23A')
    kd.delete()

    kdname_scen = KeyDatasetName.objects.using(db_alias).get(
        name="Hazard scenarios")
    kdname_scen.delete()

    kd = KeyDataset.objects.using(db_alias).get(code='BA_6')
    kd.delete()

    kd = KeyDataset.objects.using(db_alias).get(code='BA_5')
    kd.delete()

    ktag = KeyTag.objects.using(db_alias).get(name='Future projection')
    ktag.delete()

    ktag = KeyTag.objects.using(db_alias).get(name='Present')
    ktag.delete()

    ktaggrp_timeref = KeyTagGroup.objects.using(db_alias).get(
        name='time reference')
    ktaggrp_timeref.delete()


class Migration(migrations.Migration):

    dependencies = [
        ('ordd_api', '0013_migrate_schema_to_v9'),
    ]

    operations = [
        migrations.RunPython(forwards_func, backwards_func),
    ]
