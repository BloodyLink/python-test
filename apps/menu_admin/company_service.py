from .models import Company

class CompanyService():

    def getCompanies():
        return Company.objects.all()
        