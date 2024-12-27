# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class CamerasCamera(models.Model):
    id = models.BigAutoField(primary_key=True)
    location = models.CharField(max_length=255)
    status = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'cameras_camera'


class CamerasCameralog(models.Model):
    id = models.BigAutoField(primary_key=True)
    file_path = models.CharField(max_length=255)
    recorded_at = models.DateTimeField()
    camera = models.ForeignKey(CamerasCamera, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'cameras_cameralog'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey('UsersUser', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class IncidentsIncidentreport(models.Model):
    id = models.BigAutoField(primary_key=True)
    type = models.CharField(max_length=20)
    details = models.TextField()
    created_at = models.DateTimeField()
    camera = models.ForeignKey(CamerasCamera, models.DO_NOTHING, blank=True, null=True)
    sensor = models.ForeignKey('SensorsSensor', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'incidents_incidentreport'


class NotificationsNotification(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=100)
    message = models.TextField()
    is_read = models.BooleanField()
    created_at = models.DateTimeField()
    user = models.ForeignKey('UsersUser', models.DO_NOTHING)
    reason = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'notifications_notification'


class SensorsSensor(models.Model):
    id = models.BigAutoField(primary_key=True)
    type = models.CharField(max_length=20)
    location = models.CharField(max_length=255)
    status = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'sensors_sensor'


class SensorsSensorlog(models.Model):
    id = models.BigAutoField(primary_key=True)
    value = models.FloatField()
    timestamp = models.DateTimeField()
    exceeded_threshold = models.BooleanField()
    sensor = models.ForeignKey(SensorsSensor, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'sensors_sensorlog'


class Thresholds(models.Model):
    id = models.BigAutoField(primary_key=True)
    type = models.CharField(max_length=20)
    threshold_value = models.FloatField()

    class Meta:
        managed = False
        db_table = 'thresholds'


class TokenBlacklistBlacklistedtoken(models.Model):
    id = models.BigAutoField(primary_key=True)
    blacklisted_at = models.DateTimeField()
    token = models.OneToOneField('TokenBlacklistOutstandingtoken', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'token_blacklist_blacklistedtoken'


class TokenBlacklistOutstandingtoken(models.Model):
    id = models.BigAutoField(primary_key=True)
    token = models.TextField()
    created_at = models.DateTimeField(blank=True, null=True)
    expires_at = models.DateTimeField()
    user = models.ForeignKey('UsersUser', models.DO_NOTHING, blank=True, null=True)
    jti = models.CharField(unique=True, max_length=255)

    class Meta:
        managed = False
        db_table = 'token_blacklist_outstandingtoken'


class UsersUser(models.Model):
    id = models.BigAutoField(primary_key=True)
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(unique=True, max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()
    role = models.CharField(max_length=10)
    status = models.BooleanField()
    date_of_birth = models.DateField(blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users_user'


class UsersUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(UsersUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'users_user_groups'
        unique_together = (('user', 'group'),)


class UsersUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(UsersUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'users_user_user_permissions'
        unique_together = (('user', 'permission'),)
