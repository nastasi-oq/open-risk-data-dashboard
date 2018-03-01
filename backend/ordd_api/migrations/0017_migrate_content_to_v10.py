# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-08-11 11:50
from __future__ import unicode_literals

from django.db import migrations
from django.core import serializers
from django.core.management import call_command

import csv
import json


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

    #  Rename entries
    #
    #    KeyCategory
    item = KeyCategory.objects.using(db_alias).get(name='Base Data')
    item.name = 'Base data'
    item.save()

    #    KeyTag
    item = KeyTag.objects.using(db_alias).get(name='Road infrastructure')
    item.name = 'Roads'
    item.save()

    item = KeyTag.objects.using(db_alias).get(name='Harbours')
    item.name = 'Harbors'
    item.save()

    #    KeyDatasetName
    item = KeyDatasetName.objects.using(db_alias).get(name='Hazard Scenarios')
    item.name = 'Historical records of hazard events'
    item.save()

    #    KeyDatasetName
    item = KeyDatasetName.objects.using(db_alias).get(
        name='List Type Of Volcanoes')
    item.name = 'Volcanoes'
    item.save()

    #    KeyDatasetName simple capitalization
    items = KeyDatasetName.objects.using(db_alias).all()
    for item in items:
        item.name = item.name.capitalize()
        item.save()

    kd = []
    kd_code = []
    kt = []

    with open('contents/key_datasets/resilience-index-'
              'datasets-list-v10 - Datasets.csv', 'r') as kdfile,\
        open('contents/key_datasets/resilience-index-'
             'datasets-list-v10 - Tags.csv', 'r') as ktfile:
        kdcsv = csv.reader(kdfile, delimiter=',')
        ktcsv = csv.reader(ktfile, delimiter=',')

        for row in kdcsv:
            if len(row) == 0:
                continue
            kd.append(row)
            kd_code.append(row[0])
        kd = kd[1:]
        kd_code = kd_code[1:]

        for row in ktcsv:
            if len(row) == 0:
                continue
            kt.append(row)
        kt = kt[1:]

        #
        #  INSERT MISSING DATASETNAME
        #
        for keydataset in kd:
            datasetname = keydataset[2]
            print(datasetname)
            item = KeyDatasetName.objects.using(db_alias).get(name=datasetname)
        raise ValueError("Just to avoid reload")



        # keydataset

        print("\n\n")
        print("keydatasets")

        national_level = KeyLevel.objects.using(db_alias).get(name='National')

        print("\nKEYDATASETS: check keydataset not yet inserted")
        objs = KeyDataset.objects.using(db_alias).all()
        for keydataset in kd:
            for obj in objs:
                kd_cur = obj.code
                if kd_cur == keydataset[0]:
                    dsname = KeyDatasetName.objects.using(db_alias).get(
                        name=keydataset[2])
                    category = KeyCategory.objects.using(db_alias).get(
                        name=keydataset[1])
                    if obj.level_id != 2:
                        print("  WRONG LEVEL_ID: code: [%s]  level: %d"
                              % (kd_cur, obj.level_id))
                    obj.level = national_level
                    obj.description = keydataset[4]
                    obj.dataset = dsname
                    obj.category = category
                    obj.save()
                    break
            else:
                print('  Keydataset "%s" not already present in dataset.'
                      % keydataset[0])
        print("  Done")
        raise ValueError("just to avoid commit of transaction")
        # Tags

        print("\nTAGS: check tags not yet inserted")
        objs = KeyTag.objects.using(db_alias).all()
        for tag in kt:
            for obj in objs:
                tag_cur = [obj.group.name, obj.name]
                if tag_cur[0] == tag[0] and tag_cur[1] == tag[1]:
                    break
            else:
                print('  Tag "%s, %s" not already present in dataset.' % (
                    tag[0], tag[1]))
        print("  Done")

        print("\nTAGS: intersection with current dataset (old keydataset"
              " tags referenced by current dataset with new tags)")
        obj = KeyTag.objects.using(db_alias).filter(
            dataset__in=Dataset.objects.using(db_alias).filter(
                keydataset__in=kd_code)).distinct().order_by('group', 'name')
        tags_cur = [[o.group.name, o.name] for o in obj]

        for tag_cur in tags_cur:
            for tag in kt:
                if tag_cur[0] == tag[0] and tag_cur[1] == tag[1]:
                    break
            else:
                raise ValueError('Tag "%s, %s" not found in the new list.'
                                 % (tag_cur[0], tag_cur[1]))
        print("  Done")

        print("\nTAGS: check relations of tags to be removed")
        objs = KeyTag.objects.using(db_alias).all()
        for obj in objs:
            tag_cur = [obj.group.name, obj.name]
            found = False
            for tag in kt:
                if tag_cur[0] == tag[0] and tag_cur[1] == tag[1]:
                    found = True
                    break
            else:
                if (len(obj.keydataset_set.all()) != 0 or
                        len(obj.dataset_set.all()) != 0):
                    raise ValueError(
                        "Tag [%s - %s] referenced by keydataset or dataset"
                        % (tag_cur[0], tag_cur[1]))

            if found is False:
                print("  Tag [%s - %s] could be removed safety"
                      % (tag_cur[0], tag_cur[1]))









def backwards_func(apps, schema_editor):
    KeyDataset = apps.get_model("ordd_api", "KeyDataset")
    KeyCategory = apps.get_model("ordd_api", "KeyCategory")
    KeyDatasetName = apps.get_model("ordd_api", "KeyDatasetName")
    KeyTagGroup = apps.get_model("ordd_api", "KeyTagGroup")
    KeyTag = apps.get_model("ordd_api", "KeyTag")
    KeyLevel = apps.get_model("ordd_api", "KeyLevel")
    Dataset = apps.get_model("ordd_api", "Dataset")

    db_alias = schema_editor.connection.alias

    #    KeyDatasetName
    item = KeyDatasetName.objects.using(db_alias).get(
        name='Volcanoes')
    item.name = 'List Type Of Volcanoes'
    item.save()

    #    KeyDatasetName
    item = KeyDatasetName.objects.using(db_alias).get(
        name='Historical records of hazard events')
    item.name = 'Hazard Scenarios'
    item.save()

    #    KeyDatasetName simple return to titlezation
    items = KeyDatasetName.objects.using(db_alias).all()
    for item in items:
        item.name = item.name.title()
        item.save()

    #    KeyTag
    item = KeyTag.objects.using(db_alias).get(name='Harbors')
    item.name = 'Harbours'
    item.save()

    item = KeyTag.objects.using(db_alias).get(name='Roads')
    item.name = 'Road infrastructure'
    item.save()

    #    KeyCategory
    item = KeyCategory.objects.using(db_alias).get(name='Base data')
    item.name = 'Base Data'
    item.save()


class Migration(migrations.Migration):

    dependencies = [
        ('ordd_api', '0016_rename_dataset_fields'),
    ]

    operations = [
        migrations.RunPython(forwards_func, backwards_func),
    ]

