from candidate.models import Candidate


def test_creating_candidate():
    c = Candidate()

    c.create(name='a')

    e = c.events.pop()
    assert e.name == 'created'
    assert e.data == '{"name": "a"}'
    assert len(c.events) == 0
    assert c.name == 'a'


def test_update_name():
    c = Candidate()
    c.create(name='b')

    c.update_name('c')

    e = c.events.pop()
    assert e.name == 'name_updated'
    assert e.data == '{"name": "c"}'
    assert len(c.events) == 1
    assert c.name == 'c'


def test_update_email():
    c = Candidate()
    c.create(name='a')

    c.update_email('a@b.com')

    e = c.events.pop()
    assert e.name == 'email_updated'
    assert e.data == '{"email": "a@b.com"}'
    assert len(c.events) == 1
    assert c.email == 'a@b.com'
