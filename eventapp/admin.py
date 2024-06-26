from django.contrib import admin
from .models import CustomUser,Webinar,EventOrganizer,AICTE,Speaker,Program,Department,Conference,WebinarRegistration,Attendee,Service,BookService,Package,Review,ServiceProvider,Notification,ParticipationCertificate,Question,Response

admin.site.register(CustomUser)
admin.site.register(Webinar)
admin.site.register(EventOrganizer)
admin.site.register(AICTE)
admin.site.register(Program)
admin.site.register(Department)
admin.site.register(Speaker)
admin.site.register(Conference)
admin.site.register(Attendee)
admin.site.register(WebinarRegistration)
admin.site.register(Service)
admin.site.register(BookService)
admin.site.register(Package)
admin.site.register(Review)
admin.site.register(ServiceProvider)
admin.site.register(Notification)
admin.site.register(ParticipationCertificate)
admin.site.register(Question)
admin.site.register(Response)