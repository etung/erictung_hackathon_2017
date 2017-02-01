#!/bin/bash
curl -i -H "Content-Type: application/json" -X POST -d '[{"asin":"ASIN1", "category":"Dairy"},{"asin":"ASIN2","category":"Meat"}]' http://localhost:5000/packlist_creator/api/v1.0/update_inventory

