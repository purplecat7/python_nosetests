from mean_sightings import get_sightings

#print get_sightings('sightings_tab_sm.csv', 'Water')

filename = 'sightings_tab_sm.csv'

def test_water_is_correct():
    watrec, watmean = get_sightings(filename, 'waTEr')
    assert watrec==2, 'Incorrect number of records'
    assert watmean==17.0, 'Incorrect mean for water'

def test_clay_is_correct():
    clayrec, claymean = get_sightings(filename, 'Clay')
    assert clayrec==2, 'Incorrect number of records'
    assert claymean==25.5, 'Incorrect mean for clay'

def test_not_present():
    norec, nomean = get_sightings(filename, 'None')
    assert norec == 0, 'Biosig is present'
    assert nomean == 0, 'Mean for missing biosig'
