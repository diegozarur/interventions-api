from datetime import datetime


def patch_single_preprocessor(instance_id=None, data=None, **kw):
    is_all_fields_validated = all(data.get(field) for field in
                                  ["wording", "description", "name", "speaker", "location", "date_of_intervention"])
    if is_all_fields_validated:
        # Change the status to "Validated"
        data['status'] = "Validated"
    date_intervention = data.get('date_of_intervention')
    if date_intervention:
        date_str = date_intervention.split('T')[0]
        date_obj = datetime.strptime(date_str, '%Y-%m-%d')

        if date_obj < datetime.now() and is_all_fields_validated:
            data['status'] = 'Completed'

    return instance_id
