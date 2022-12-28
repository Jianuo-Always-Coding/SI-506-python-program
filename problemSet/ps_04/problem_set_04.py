# START PROBLEM SET 4
print('Problem Set 4 \n')

employers = [
    "Company Name, Location, Number of Employees, Website, Industry",
    "Adobe Systems, California, 25000, http://www.adobe.com, software",
    "Bloomberg, New York, 25000, http://careers.bloomberg.com, Financial",
    "Boston university, Massachusetts, 25000, http://www.bu.edu, Education",
    "Chewy, Florida, 25000, https://careers.chewy.com/us/en/c/student-program, ecommerce",
    "DHL Consulting, Florida, 200, http://www.dhl-consulting.com, Consulting",
    "Fisher Investments, Washington, 5000, http://www.fishercareers.com, financial",
    "Gartner, Connecticut, 25000, http://jobs.gartner.com, consulting",
    "Gallagher, Illinois, 25000, https://jobs.ajg.com/, Insurance",
    "Guidehouse, Virginia, 25000, https://guidehouse.com, Consulting",
    "Kohl's, Wisconsin, 25000, https://careers.kohls.com/internships, Retail",
    "Meijer, Michigan, 25000, https://jobs.meijer.com, retail",
    "Morningstar, Illinois, 10000, http://www.morningstar.com, Financial",
    "Neon Financial, Illinois, 10, https://www.neonforlife.com, Financial",
    "Northwestern Medicine, Illinois, 25000, https://jobs.nm.org/, Healthcare",
    "Point72, Connecticut, 1000, http://www.Point72.com, Financial",
    "Procter & Gamble (P&G), Ohio, 25000, https://www.pgcareers.com, Consumer Packaged Goods",
    "Samsung SDI America, Michigan, 1000, https://www.samsungsdi.com, Manufacturing",
    "Sun Communities, Michigan, 5000, http://www.suncommunities.com, Real Estate",
    "TOPIT, Texas, 10, http://www.topit.co, Software",
    "TikTok, California, 10000, https://careers.tiktok.com/campus, Software",
    "Uline, Wisconsin, 10000, https://www.uline.jobs, Wholesale Trade",
    "University of Michigan International Center, Michigan, 50, http://internationalcenter.umich.edu, Education",
    "Veeam Software, Georgia, 5000, https://careers.veeam.com, Software",
    "Welltower, Ohio, 1000, http://www.welltower.com, Real Estate"
]

# PROBLEM 01
print('\nPROBLEM 1')
for i in range(len(employers)):
    employers[i] = employers[i].split(", ")

# print(employers)

header = employers[0]
# print(f"\nHeader row = {header}")

# PROBLEM 02
print('\nPROBLEM 2')
universities = []
other_companies = []

for employer in employers[1:]:
    if employer[4] == "Education":
        universities.append(employer)
    else:
        other_companies.append(employer)

# print(f"\nuniversities = {universities}")
# print(f"\nother_companies = {other_companies}")

# PROBLEM 03
print('\nPROBLEM 3')
financial = []
software = []
real_estate = []
consulting = []
other_industry = []

for company in other_companies:
    if (company[4].lower() == "financial"):
        financial.append(company[0])
    elif (company[4].lower() == "software"):
        software.append(company[0])
    elif (company[4].lower() == "real estate"):
        real_estate.append(company[0])
    elif (company[4].lower() == "consulting"):
        consulting.append(company[0])
    else:
        other_industry.append(company[0])




# print(f"\nfinancial = {financial}")
# print(f"\nsoftware = {software}")
# print(f"\nreal_estate = {real_estate}")
# print(f"\nconsulting = {consulting}")
# print(f"\nother_industry = {other_industry}")

# PROBLEM 04
print('\nPROBLEM 4')
smallest_companies = []
least_num_employees = float('inf')

for company in other_companies:
    num_employees = int(company[2])
    if (num_employees < least_num_employees):
        least_num_employees = num_employees
        smallest_companies.clear()
        smallest_companies.append(company[0])
    elif (num_employees == least_num_employees):
        smallest_companies.append(company[0])

# print(f"\nsmallest_companies = {smallest_companies}")

# PROBLEM 05
print('\nPROBLEM 5')

salaries = """Adobe; Computer Scientist; 262012
Adobe; Data Analyst; 121390
TikTok; Policy Analyst; 107240
Fisher Investments; Portfolio Analyst; 97349
Bloomberg; senior data Analyst; 166267
Procter & Gamble; Data Scientist; 142429
Adobe; Research Scientist; 248819
Chewy; Software Engineer; 153402
Morningstar; Financial Analyst; 86022
Morningstar; Software Engineer; 124599
TikTok; Software Engineer; 188801
Fisher Investments; Financial Analyst; 99365
TikTok; data Analyst; 109457
Bloomberg; Software Engineer; 182015
Procter & Gamble; Data Analyst; 103472
TikTok; Designer; 114163
"""

salary_list = []
# print(salarySplit)
salary_list = salaries.splitlines()
for i in range(len(salary_list)):
    salary_list[i] = salary_list[i].split("; ")

# print(f'\nsalary_list = {salary_list}')


# PROBLEM 06
print('\nPROBLEM 6')

da_salary = []
idx = 0

while idx < len(salary_list):
    # if "data analyst" or "senior data analyst" in salary_list[idx][1].lower():
    #     da_salary.append(int(salary_list[idx][2]))
    if "data analyst" in salary_list[idx][1].lower():
        da_salary.append(int(salary_list[idx][2]))
    elif "senior data analyst" in salary_list[idx][1].lower():
        da_salary.append(int(salary_list[idx][2]))
    idx = idx + 1

# print(f"\nda_salary = {da_salary}")
avg_da_salary = sum(da_salary) / len(da_salary)
# print(f"\navg_da_salary = {avg_da_salary}")

# PROBLEM 07
# 
idx = 0
while(idx < len(salary_list)):
    if(int(salary_list[idx][2]) < 100000):
        company_salary = (salary_list[idx][0],int(salary_list[idx][2]))
        break
    idx = idx + 1
# print(company_salary)
# END PROBLEM SET
if None: 
    print("dd")