from rest_framework import routers
from offers import views as offers_views
from escrows import views as escrows_views
from coosta_users import views as user_views
from coosta_email import views as email_views
from properties import views as property_views
from contracts import views as contracts_views
from statistic import views as statistics_views
from coosta_messages import views as message_views
from appointments import views as appointment_views
from coosta_notification import views as notification_views
from flags import views as flag_views

router = routers.DefaultRouter()

# Users Router
router.register(r'users', user_views.UserViewSet)
router.register(r'user_profile', user_views.UserProfileViewSet, 'userprofile')
router.register(r'non_pre_approved_user', user_views.NonPreApprovedUserViewSet,
                'non_pre_approved_user')
router.register(r'documents', user_views.DocumentsViewSet, 'documents')
router.register(r'pre_approved_user', user_views.PreApprovedUserViewSet,
                'pre_approved_user')
router.register(r'pre_approved_document',
                user_views.PreApprovedDocumentsViewSet,
                'pre_approved_document')

# Property Router
router.register(r'property', property_views.PropertyViewSet, 'property')
router.register(r'propertystatus', property_views.PropertyStatusViewSet,
                'propertystatus')
router.register(r'property_images', property_views.PropertyImagesViewSet,
                'propertyimages')
router.register(r'images', property_views.ImagesViewSet, 'images')
router.register(r'shortlisted_property',
                property_views.ShortlistedPropertyViewSet,
                'shortlistedproperty')
router.register(r'recommended_properties',
                property_views.RecommendedPropertyViewSet,
                'recommended_properties')

# Parcel Router
router.register(r'parcel', property_views.ParcelViewSet, 'parcel')

# Groups Router
router.register(r'groups', user_views.GroupViewSet)

# Message Router
router.register(r'message', message_views.CoostaMessageViewSet,
                'coosta_message')

# Email Router
router.register(r'send_email', email_views.SendEmailView, 'send_email')
router.register(r'password_reset', email_views.PasswordResetView,
                'password_reset')
router.register(r'password_reset_confirm',
                email_views.PasswordResetConfirmView,
                'password_reset_confirm')

# Notification Router
router.register(r'notification', notification_views.NotificationViewSet,
                'coostanotification')
router.register(r'notification_type',
                notification_views.NotificationTypeViewSet,
                'notificationtype')

# Statistics
router.register(r'statistics', statistics_views.PageViewSet, 'pageview')

# Contracts
router.register(r'contract', contracts_views.ContractViewSet, 'contract')

# Offers
router.register(r'offers', offers_views.OffersViewSet, 'offers')

# CounterOffers
router.register(r'counteroffers', offers_views.CounterOffersViewSet,
                'counteroffers')

# Escrows
router.register(r'escrowproperty', escrows_views.EscrowPropertyViewSet,
                'escrowproperty')

# Appointments
router.register('openhouse', appointment_views.OpenHouseViewSet, 'openhouse')
router.register('openhousersvp', appointment_views.OpenHouseRSVPViewSet,
                'openhousersvp')
router.register('owneravailability',
                appointment_views.OwnerAvailabilityViewSet,
                'owneravailability')
router.register('appointmentrequest',
                appointment_views.AppointmentRequestViewSet,
                'appointmentrequest')

# Flags
router.register('flagtype', flag_views.FlagTypeViewSet, 'flagtype')
router.register('flaggedproperty', flag_views.FlaggedPropertyViewSet,
                'flaggedproperty')