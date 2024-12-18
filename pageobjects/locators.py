
from selenium.webdriver.common.by import By

class LocatorsHomePage():
    
    # txt_hpg_headline_x =(By.XPATH,"//h1[normalize-space()='Innovative Softwareentwicklung']")
    txt_hpg_headline_x =(By.XPATH, "//div[@class='home_banner_headings']/h1[.='Innovative Software Development']")
    btn_Hamburger_hmpg_x=(By.XPATH, "//div[@class='side_menu_button']")

    #Project section:
    # carousel1_proj_x=(By.XPATH,"//ol[@class='carousel-indicators']/li[@aria-labelledby='slide-projectSlide-1']")
    # carousel1_proj_x=(By.XPATH,"//ol[@class='carousel-indicators']/li[@aria-labelledby='slide-projectSlide-1'] [@class='ng-star-inserted active']")
    carousel_1_proj_x=(By.XPATH,"//div[@id='project']//li[1]")
    carousel1_text_assert=(By.XPATH, "//h3[normalize-space()='ImmoSpice']")
    carousel_2_proj_x=(By.XPATH,"//div[@id='project']//li[2]")
    carousel2_text_assert=(By.XPATH, "//h3[normalize-space()='Viasuisse']")
    carousel_3_proj_x=(By.XPATH,"//div[@id='project']//li[3]")
    carousel3_text_assert=(By.XPATH, "//h3[normalize-space()='Prozessraum']")

    #Services section:
    services_heading_x=(By.XPATH,"//h1[normalize-space()='Services']")
    # service_card_1=(By.XPATH,"(//div[@class='flip-card'])[1]")
    # service_card_1=(By.XPATH,"(//div[@class='service_card_header card_header text-black font-weight-700 fontSize-4_0 text-uppercase'])[1]")
    
    assert_card_design=(By.XPATH, "//div[normalize-space()='DESIGN']")
    service_card_1=(By.XPATH,"(//div[@class='flip-card-front'])[1]")
    
    assert_card_consultancy=(By.XPATH, "//div[normalize-space()='Consultancy']")
    service_card_2=(By.XPATH,"(//div[@class='flip-card-front'])[2]")

    assert_card_sharepoint=(By.XPATH, "//div[normalize-space()='SHAREPOINT']")
    service_card_3=(By.XPATH,"(//div[@class='flip-card-front'])[3]")

    assert_card_engineering=(By.XPATH, "//div[normalize-space()='ENGINEERING']")
    service_card_4=(By.XPATH,"(//div[@class='flip-card-front'])[4]")

    assert_card_QA=(By.XPATH,"//div[normalize-space()='QUALITY-ASSURANCE']")
    service_card_5=(By.XPATH,"(//div[@class='flip-card-front'])[5]")

    assert_card_salesforce=(By.XPATH,"//div[normalize-space()='SALESFORCE CRM']")
    service_card_6=(By.XPATH,"(//div[@class='flip-card-front'])[6]")
    flip_6cards=(By.XPATH,"//div[@class='row no-gutters-sm container-fluid justify-content-center service_card_row_padding']//div[@class='flip-card-front']")
    text_flip_6cards=(By.XPATH,"//p[@class='text-grey mb-0 fontSize-2_4 mt-20'][text()]")

    card1_design=(By.XPATH, "//div[normalize-space()='DESIGN']")
    card1_text=(By.XPATH, "//p[@class='text-grey mb-0 fontSize-2_4 mt-20'][contains(text(),'Intuitive - Attractive and simple user interface t')]")
                  
    #Clients section
    clients_carousels_x=(By.XPATH, "//div[@class='col-xl-6 col-md-12']//li")
    clients_carousel1_x=(By.XPATH, "//div[@class='col-xl-6 col-md-12']//li[1]")
    clients_carousel2_x=(By.XPATH, "//div[@class='col-xl-6 col-md-12']//li[2]")
    clients_carousel3_x=(By.XPATH, "//div[@class='col-xl-6 col-md-12']//li[3]")
    clients_carousel4_x=(By.XPATH, "//div[@class='col-xl-6 col-md-12']//li[4]")
    clients_carousel5_x=(By.XPATH, "//div[@class='col-xl-6 col-md-12']//li[5]")
    clients_carousel6_x=(By.XPATH, "//div[@class='col-xl-6 col-md-12']//li[6]")

    clients_crsl1_name_assert=(By.XPATH, "//h2[normalize-space()='Martin Küng']")
    # clients_crsl1_des_assert=(By.XPATH, "(//h3[@class='fontSize-3_0 text-light-black mb-0 font-weight-400'])[1]")

    clients_crsl2_name_assert=(By.XPATH, "//h2[normalize-space()='Thomas Hirsiger']")
    clients_crsl2_des_assert=(By.XPATH, "(//h3[normalize-space()='CEO @ ASAGO'])[1]")

    clients_crsl3_name_assert=(By.XPATH, "//h2[normalize-space()='Doman Obrist']")
    clients_crsl3_des_assert=(By.XPATH, "//h3[normalize-space()='Co Founder @ Reach']")

    clients_crsl4_name_assert=(By.XPATH, "//h2[normalize-space()='Daniel Gasser']")
    clients_crsl4_des_assert=(By.XPATH, "//h3[normalize-space()='@ Bouygues Energies & Services']")

    clients_crsl5_name_assert=(By.XPATH, "//h2[normalize-space()='M. Lara Ferrari']")
    clients_crsl5_des_assert=(By.XPATH, "//h3[normalize-space()='CEO @ Prozessraum Ltd']")

    clients_crsl6_name_assert=(By.XPATH, "//h2[normalize-space()='Damian Birch']")
    clients_crsl6_des_assert=(By.XPATH, "//h3[normalize-space()='Head of Solutions & Technology @ Viasuisse AG']")

    # clients_names_assert=(By.XPATH, "//h2[@class='fontSize-3_0 text_black mb-0 font-weight-800 text-uppercase']")
    
    clients_slides_12elements=(By.XPATH,"//ngb-carousel[@class='carousel slide client_carousel_slides client_carousel_indicator_height']//div[@class='row justify-content-sm-center ng-star-inserted']/div[@class='col mb-30']//descendant::img[@alt]")
    # text_of_12clientcards=((By.XPATH, "//ngb-carousel[@class='carousel slide client_carousel_slides client_carousel_indicator_height']//div[@class='row justify-content-sm-center ng-star-inserted']/div[@class='col mb-30']//descendant::img").get_attribute("alt"))

    #Footer section:
    footer_headline=(By.XPATH, "//h1[normalize-space()='GET IN TOUCH']")
    footer_assert_switzerland=(By.XPATH, "//h2[normalize-space()='SWITZERLAND']")
    footer_assert_br_Ind_mang=(By.XPATH, "//h2[normalize-space()='INDIA - Mangalore']")
    footer_assert_br_canada=(By.XPATH, "//h2[normalize-space()='CANADA']")
    footer_assert_br_Ind_bang=(By.XPATH, "//h2[normalize-space()='INDIA - Bangalore']")
    footer_assert_company_name=(By.XPATH, "//div[@class='flagadd_information']//div[2]//div[1]//div[2]//p[1]")
    footer_assert_mail_address=(By.XPATH, "//body[1]/app-root[1]/app-layout[1]/div[1]/app-home[1]/div[1]/div[5]/app-footer[1]/div[1]/div[2]/div[3]/div[1]/div[1]/div[1]/div[1]/p[2]/a[1]")
    footer_end_text=(By.XPATH,"//p[@class='text-white fontSize-2_0 text-center pb-30 mb-0'] [.=' Copyright © 2022 BixBytes Solutions ']")
    
    footer_insta_link=(By.XPATH,"//h2[normalize-space()='Instagram']")
    footer_fb_link=(By.XPATH,"//h2[normalize-space()='Facebook']")
    footer_twitter_link=(By.XPATH,"//h2[normalize-space()='Twitter']")
    footer_linkedin_link=(By.XPATH,"//h2[normalize-space()='LinkedIn']")

    footer_contact_num_link=(By.XPATH,"/html[1]/body[1]/app-root[1]/app-layout[1]/div[1]/app-home[1]/div[1]/div[5]/app-footer[1]/div[1]/div[2]/div[3]/div[1]/div[1]/div[1]/div[1]/p[1]/a[1]")
    footer_mail_address_link=(By.XPATH,"//div[@class='row mb-lg-130 mb-md-70 mb-40 lg_flagged_information']//div[1]//div[1]//div[1]//p[2]//a[1]")
    
class LocatorsMenu():
    menu_main_modules=(By.XPATH, "//div[@class='border_left w-100 h-100 d-flex align-tems-center']/ul/li/a/span")
    # menu_main_modules=(By.XPATH, "//li/a/span")
    # menu_main_modules=(By.XPATH, "/html[1]/body[1]/app-root[1]/app-layout[1]/div[1]/app-home[1]/side-menu[1]/div[1]/div[1]/div[1]/div[2]/div[1]/ul[1]/li/a[1]/span")
    menu_close_btn=(By.XPATH, "//div[@class='side_menu_button active_menu']")

    menu_home_link=(By.XPATH, "//span[@data-title='Home']")
    menu_company_link=(By.XPATH, "//span[@data-title='Company']")
    menu_services_link=(By.XPATH, "//span[@data-title='Services']")
    menu_designlab_link=(By.XPATH, "//span[@data-title='Design Lab']")
    # menu_blog_link=(By.XPATH, "//span[@data-title='Blog']")
    menu_blog_link=(By.XPATH, "//div[@class='border_left w-100 h-100 d-flex align-tems-center']/ul/li/a/span[@data-title='Blog']")
    menu_jobs_link=(By.XPATH, "//span[@data-title='Jobs']")
    menu_contact_link=(By.XPATH, "//span[@data-title='Contact']")

    menu_GTC_link=(By.XPATH, "//span[normalize-space()='GTC']")
    menu_GTC_download=(By.XPATH, "//div[@class='col-12 col-md-8']//div[1]//div[1]//a[1]//span[1]")
    menu_Privacypolicy_link=(By.XPATH, "//span[normalize-space()='Privacy Policy']")
    menu_SiteMap_link=(By.XPATH, "//a[normalize-space()='Site Map']")

    menu_insta_link=(By.XPATH, "//div[@class='footer_section']//li[1]//a[1]")
    menu_fb_link=(By.XPATH, "//img[@src='assets/image/fb.svg']")
    menu_twitter_link=(By.XPATH, "//img[@class='twitter_icon']")
    menu_linkedin_link=(By.XPATH, "//img[@src='assets/image/linkedin-main.svg']")
    
    menu_lang_change_DE=(By.XPATH, "//a[normalize-space()='DE']")
    txt_hpg_DE_headline=(By.XPATH, "//h1[.='Innovative Softwareentwicklung']")
    txt_hpg_DE_project=(By.XPATH, "//h1[.='PROJEKTE']")
    txt_hpg_DE_services=(By.XPATH, "//h1[.='DIENSTLEISTUNGEN']")
    txt_hpg_DE_clients=(By.XPATH, "//h1[.='KUNDEN']")
    txt_hpg_DE_footer_hline=(By.XPATH, "//h1[normalize-space()='KONTAKT AUFNEHMEN']")

class LocatorsCompany():

    hamburger_company_page_x=(By.XPATH, "//div[@class='button_hand']")
    headline_company_page=(By.XPATH, "//h1[normalize-space()='The Principles that matter most']")
    who_v_r_company_page=(By.XPATH, "//span[normalize-space()='Who we are']")
    asrt_y_bbs=(By.XPATH, "//h1[normalize-space()='Why Bix Bytes Solutions?']")
    asrt_work_culture=(By.XPATH, "//h1[normalize-space()='Our Work Culture']")
    asrt_client_meeting=(By.XPATH, "//h1[normalize-space()='Client Meetings @ BBS']")
    # work_culture_slides=(By.XPATH, "//div[@class='bbs_lifewrapper']/descendant::ol/li")
    work_culture_slides=(By.XPATH, "//ngb-carousel[@class='carousel slide bbs_carousel_wrapper']//li")
    wt_v_do_company_page=(By.XPATH, "//span[normalize-space()='What we do']")
    y_bbs_icon_company_page=(By.XPATH, "//span[normalize-space()='Why BBS']")
    y_bbs_hdline_company_page=(By.XPATH, "//h1[normalize-space()='Why Bix Bytes Solutions?']")
    footer_endtext_company_page=(By.XPATH, "//p[@class='text-white fontSize-2_0 text-center pb-30 mb-0']")
    footer_mailaddress_company_page=(By.XPATH, "//div[@class='row mb-lg-130 mb-md-70 mb-40 lg_flagged_information']//div[1]//div[1]//div[1]//p[2]//a[1]")
    footer_contact_num_link_cp=(By.XPATH,"//p[@class='mb-0 mt-md-30']//a[@class='text-white fontSize-2_0 font-weight-400 no-anchor'][normalize-space()='+ 41 44 552 96 90']")

class LocatorsServices():
   
    hamburger_service_page_x=(By.XPATH, "//div[@class='button_hand']")
    services_headline_x=(By.XPATH, "//h1[normalize-space()='Services we provide']")
    services_menu_5icons=(By.XPATH, "//div[@class='bbs_activetab service_tab']")
    our_services_tab=(By.XPATH, "//span[normalize-space()='Our Services']")
    our_services_7headlines=(By.XPATH, "//h2[@class='fontSize-4_0']")
    our_services_6readmore_links=(By.XPATH, "//a[@class='d-flex justify-content-end fontSize-2_4 font-weight-400']")

    salesforce_crm_tab=(By.XPATH, "//span[normalize-space()='Salesforce CRM']")
    salesforce_crm_heading=(By.XPATH, "//h2[normalize-space()='Your Salesforce Partner for success']")
    salesforce_crm_7headlines=(By.XPATH, "//h2[@class='fontSize-4_0']")
    salesforce_5readmore_links=(By.XPATH, "//a[@class='d-flex justify-content-end fontSize-2_4 font-weight-400']")
    salesforce_6th_readmore_links=(By.XPATH, "//a[@class='d-flex justify-content-end fontSize-2_4 font-weight-400 read_more_align english_text']")

    our_values_tab=(By.XPATH, "//span[normalize-space()='Our Values']")
    our_values_3headlines=(By.XPATH, "//h2[@class='fontSize-4_0']")
    our_expertise_tab=(By.XPATH, "//span[normalize-space()='Our Expertise']")
    our_exprts_4headlines=(By.XPATH, "//div[@class='Our_Expertise_wrapper mb-20']/h1")
    agile_framework_tab=(By.XPATH, "//span[normalize-space()='Agile Framework']")
    hdline_agile_framework=(By.XPATH, "//h1[normalize-space()='Agile framework']")
    hdlines3_agile_framework=(By.XPATH, "//div[@class='mat_Expertise_tab container']//h2")
    link_soft_dev_af=(By.XPATH, "//a[normalize-space()='software development']")
    link_proj_mgmnt_af=(By.XPATH, "//a[normalize-space()='project management']")
    link_scrum_defn_af=(By.XPATH, "//a[normalize-space()='https://scrumguides.org/scrum-guide.html']")

    assert_our_process_sec=(By.XPATH, "/html[1]/body[1]/app-root[1]/app-layout[1]/div[1]/app-our-service[1]/app-our-process[1]/section[1]/div[1]/div[1]/h1[1]")
    asrt_7process_testing=(By.XPATH, "//div[@class='order-2 order-xl-2 col-12 col-xl-auto col-md-12 col-sm-12 right_side ng-tns-c98-4']/ul/li/span[@class='fontSize-3_0 ng-tns-c98-4']")
    lets_discuss_sec_heline=(By.XPATH, "//h2[@class='header_underline white_underline middle_line wordmiddle_line text-center text-black mt-150 fontSize-6_0 font-weight-600']")
    name_field_lets_sec=(By.XPATH, "//input[@placeholder='Name']")
    email_field_lets_sec=(By.XPATH, "//input[@placeholder='Email']")
    checkbox_lets_sec=(By.XPATH, "//div[@class='recaptcha-checkbox-border']")
    btn_get_touch_lets=(By.XPATH, "//span[@id='basic-addon2']")
    empty_field_warning_msg=(By.XPATH,"//div[@class='text-danger ml-3 mt-3 let_us_discuss_err_msg fontSize-2_0 ng-star-inserted']")
    captch_warning_msg=(By.XPATH, "//div[@class='ng-star-inserted']")

class LocatorsBlog():
    #Featured Article:
    hamburger_blog_page_x=(By.XPATH, "//div[@class='button_hand']")
    txt_featured_article=(By.XPATH, "//h2[normalize-space()='FEATURED ARTICLE']")
    btns3_shr_icon_featured_art=(By.XPATH, "//div[@class='right_project_card']//li//button[@type='button']//*[name()='svg']")
    share_icon_featured_art=(By.XPATH, "(//div[@class='blog_share_socialmedia'])[1]")
    share_icon_linkedin=(By.XPATH, "//div[@class='right_project_card']//li[@class='linkedin_btn btn_outer']//button[@type='button']//*[name()='svg']//*[name()='path' and @id='XMLID_192_']")
    share_icon_twitter=(By.XPATH, "//div[@class='right_project_card']//li[@class='twitter_btn btn_outer']//button[@type='button']//*[name()='svg']")
    share_icon_fb=(By.XPATH, "//div[@class='right_project_card']//li[@class='facebook_btn btn_outer']//button[@type='button']")
    read_more_fea_artcle=(By.XPATH, "//a[@class='text_info font-weight-400 fontSize-2_0 cursor-pointer text-uppercase']")
    fea_artcle_detailpage_hdline=(By.XPATH, "//h1[contains(text(),'Top Technological Trends Transforming Various Indu')]")
    back_to_blog=(By.XPATH, "//a[normalize-space()='Back to Blog']")

    social_web_links_detailpage=(By.XPATH, "//li[@class='facebook_btn btn_outer']//button[@type='button']//*[name()='svg']")
    social_web_fb_detpage=(By.XPATH,"//li[@class='facebook_btn btn_outer']//button[@type='button']")
    social_web_twit_detpage=(By.XPATH,"//li[@class='twitter_btn btn_outer']//button[@type='button']//*[name()='svg']")
    social_web_linkedin_detpage=(By.XPATH,"//li[@class='linkedin_btn btn_outer']//button[@type='button']//*[name()='svg']")
    
    #Recent article:
    txt_recent_article=(By.XPATH, "/html[1]/body[1]/app-root[1]/app-layout[1]/div[1]/app-blog[1]/app-recent-article[1]/div[1]/div[2]/div[3]/div[1]/div[1]/div[3]/div[2]/div[1]/h2[1]")
    share_icon_recent_art1=(By.XPATH, "(//div[@class='blog_share_socialmedia'])[2]")
    linkedin_recent_art1=(By.XPATH, "//div[@class='col-xl order-xl-0']//li[@class='linkedin_btn btn_outer']//button[@type='button']")
    twitter_recent_art1=(By.XPATH, "//div[@class='col-xl order-xl-0']//li[@class='twitter_btn btn_outer']//button[@type='button']")
    fb_recent_art1=(By.XPATH,"//div[@class='col-xl order-xl-0']//li[@class='facebook_btn btn_outer']//button[@type='button']//*[name()='svg']")
    all_websites_rec_art1=(By.XPATH, "//div[@class='col-xl order-xl-0']//li//button[@type='button']")
    readmore_rcnt_art1=(By.XPATH, "//a[@href='/en/blog-detail/empowering-women-to-excel-in-work-and-personal-life']")

    share_icon_recent_art2=(By.XPATH, "(//div[@class='blog_share_socialmedia'])[3]")
    linkedin_recent_art2=(By.XPATH, "//div[@class='col-xl order-xl-0 order-xl-2']//li[@class='linkedin_btn btn_outer']//button[@type='button']")
    twitter_recent_art2=(By.XPATH, "//div[@class='col-xl order-xl-0 order-xl-2']//li[@class='twitter_btn btn_outer']//button[@type='button']")
    fb_recent_art2=(By.XPATH,"//div[@class='col-xl order-xl-0 order-xl-2']//li[@class='facebook_btn btn_outer']//button[@type='button']")
    all_websites_rec_art2=(By.XPATH, "//div[@class='col-xl order-xl-0 order-xl-2']//li//button[@type='button']//*[name()='svg']")
    readmore_rcnt_art2=(By.XPATH, "/html[1]/body[1]/app-root[1]/app-layout[1]/div[1]/app-blog[1]/app-recent-article[1]/div[1]/div[2]/div[4]/div[1]/div[1]/div[3]/div[2]/div[1]/div[1]/a[1]")

    txt_all_articles=(By.XPATH, "//h2[normalize-space()='All Articles']")
    search_bar_all_artcl=(By.XPATH, "//input[@placeholder='Search for articles']")
    back_arrow_all_artcl=(By.XPATH,"//img[@src='assets/image/Arrow_left.svg']")
    frw_arrow_all_artcl=(By.XPATH,"//img[@src='assets/image/Arrow_right.svg']")
    share_icon_aa1=(By.XPATH,"(//div[@class='blog_share_socialmedia'])[4]")
    share_icon_aa2=(By.XPATH,"(//div[@class='blog_share_socialmedia'])[5]")
    share_icon_aa3=(By.XPATH,"(//div[@class='blog_share_socialmedia'])[6]")
    share_icon_aa4=(By.XPATH,"(//div[@class='blog_share_socialmedia'])[7]")
    share_icon_aa5=(By.XPATH,"(//div[@class='blog_share_socialmedia'])[8]")
    share_icon_aa6=(By.XPATH,"(//div[@class='blog_share_socialmedia'])[9]")
    all_art_6read_more=(By.XPATH,"//a[@class='read_more font-weight-4000 fontSize-2_0 cursor-pointer text-uppercase'] [text()=' READ MORE ']")

class LocatorsJobs():

    hamburger_jobs_page_x=(By.XPATH, "//div[@class='button_hand']")
    job_page_1line=(By.XPATH, "//h2[normalize-space()='IT Project Lead (PHP)']")
    jobs_12read_more=(By.XPATH, "//div[@class='job_article_main mt-60 position-relative']//a[@class='read_more fontSize-2_4 font-weight-400']")
    btn_back_to_jobs=(By.XPATH, "//a[normalize-space()='Back to Jobs']")
    txt_all_job_openings=(By.XPATH,"//h2[normalize-space()='All Job Openings']")
    all_openings_job_cards=(By.XPATH,"//a[@class='read_more font-weight-4000 fontSize-2_0 cursor-pointer text-uppercase']")
    footer_mail_link=(By.XPATH,"//div[@class='row mb-lg-130 mb-md-70 mb-40 lg_flagged_information']//div[1]//div[1]//div[1]//p[2]//a[1]")
    footer_contact_link=(By.XPATH,"//p[@class='mb-0 mt-md-30']//a[@class='text-white fontSize-2_0 font-weight-400 no-anchor'][normalize-space()='+ 41 44 552 96 90']")

    # asrt_job_detpag_position=(By.XPATH,"//span[normalize-space()='Position:']")
    # asrt_job_detpag_position=(By.XPATH,"//span[normalize-space()='Qualification:']")
    # asrt_job_detpag_position=(By.XPATH,"//span[normalize-space()='Experience:']")
    # asrt_job_detpag_position=(By.XPATH,"//span[normalize-space()='Location:']")
    # asrt_job_detpag_position=(By.XPATH,"//p[normalize-space()='Our Company']")
    # asrt_job_detpag_position=(By.XPATH,"//p[normalize-space()='We Offer']")
    # asrt_job_detpag_position=(By.XPATH,"//p[normalize-space()='Responsibilities:']")
    # asrt_job_detpag_position=(By.XPATH,"//p[normalize-space()='You Offer:']"
    jobs_read_more_12th=(By.XPATH,"(//a[@class='read_more font-weight-4000 fontSize-2_0 cursor-pointer text-uppercase'])[10]")
    
    asrt_job_detpag_hdline=(By.XPATH,"//h2[normalize-space()='Current Openings']")
    asrt_job_detpag_txt1=(By.XPATH,"//div[@class='mb-25']//span[@class='job_info_important mb-10']")
    asrt_job_detpag_txt2=(By.XPATH,"//div[@class='mb-25']//span[@class='job_info_important mb-10 ng-star-inserted']")
    asrt_job_detpag_txt3=(By.XPATH,"//div[@class='mb-25']//p[@class='job_info_important fontSize-2_4']")
    asrt_job_detpag_txt4=(By.XPATH,"//div[@class='mb-25']//p[@class='job_info_important fontSize-2_4 ng-star-inserted']")
    jop_application_heading=(By.XPATH,"//h2[normalize-space()='Apply for this position']")
    # job_aplcn_first_name=(By.XPATH,"//input[@id='mat-input-10'][@class='mat-input-element mat-form-field-autofill-control ng-tns-c48-11 ng-pristine ng-invalid cdk-text-field-autofill-monitored ng-touched']")
    job_aplcn_first_name=(By.XPATH, "//input[@formcontrolname='firstName']")
    # job_aplcn_first_name=(By.ID, "//input[@id='mat-input-10']")
    # job_aplcn_last_name=(By.XPATH,"//input[@id='mat-input-11'][@class='mat-input-element mat-form-field-autofill-control ng-tns-c48-12 ng-pristine ng-invalid cdk-text-field-autofill-monitored ng-touched']")
    job_aplcn_last_name=(By.XPATH,"//input[@formcontrolname='lastName']")
    job_aplcn_last_name=(By.XPATH,"//input[@formcontrolname='lastName']")
    job_aplcn_email=(By.XPATH,"//input[@formcontrolname='email']")
    job_aplcn_phone=(By.XPATH,"//input[@formcontrolname='phone']")
    # upload_resume=(By.XPATH,"//input[@type='file'] [@id='resumeUpload']")
    upload_resume=(By.XPATH,"//img[@alt='Upload Your Resume']")
    click_ch_box=(By.XPATH,"//span[@class='recaptcha-checkbox goog-inline-block recaptcha-checkbox-unchecked rc-anchor-checkbox']")
    job_aplcn_portfolio=(By.XPATH,"//span[@class='mat-form-field-label-wrapper ng-tns-c48-5']")
    job_aplcn_submit_btn=(By.XPATH,"//button[normalize-space()='Submit']")
    warning_msg1_aplcn_form=(By.XPATH,"//span[@class='d-block ng-star-inserted']")
    warning_msg_last_name=(By.XPATH,"//mat-error[@id='mat-error-2']")
    warning_msg_phnum=(By.XPATH,"//mat-error[@id='mat-error-3']")
    warning_msg_uploadfile=(By.XPATH,"//div[@class='fileupload_erro_txt mb-10 ng-star-inserted']")
    warning_msg_captcha=(By.XPATH,"//div[@class='ng-star-inserted']")
    error_msg_invalid_mailid=(By.XPATH, "//span[@class='d-block ng-star-inserted']")
    error_msg_invalid_phn_num=(By.XPATH, "//mat-error[@id='mat-error-4']")
    jop_aplcn_footer_txt=(By.XPATH, "//a[normalize-space()='hr@bixbytessolutions.com']")

class LocatorsContact():
    contact_page_hdline=(By.XPATH,"//h1[normalize-space()='Contact Us']")
    hamburger_contact_page=(By.XPATH,"//div[@class='side_menu_button']")

    contpage_name_txtfield=(By.XPATH, "//input[@id='mat-input-0']")
    contpage_email_txtfield=(By.XPATH, "//input[@id='mat-input-1']")
    contpage_phnnum_txtfield=(By.XPATH, "//input[@id='mat-input-2']")
    contpage_proj_txtfield=(By.XPATH, "//input[@id='mat-input-3']")
    contpage_des_txtfield=(By.XPATH, "//input[@id='mat-input-4']")
    contpage_chbox_captcha=(By.XPATH, "//span[@class='recaptcha-checkbox goog-inline-block recaptcha-checkbox-unchecked rc-anchor-checkbox']")
    contpage_lets_dscs_btn=(By.XPATH, "//button[@class='btn_lets_discuss cursor-pointer fontSize-3_0 mt-60']")

    contpage_warmsg_name=(By.XPATH,"//span[normalize-space()='Name is required']")
    contpage_warmsg_email=(By.XPATH,"//span[normalize-space()='E-mail address is required']")
    contpage_warmsg_phnnum=(By.XPATH,"//span[normalize-space()='Phone number is required']")
    contpage_warmsg_proj=(By.XPATH,"//span[normalize-space()='Project name is required']")
    contpage_warmsg_description=(By.XPATH,"//span[normalize-space()='Description is required']")
    contpage_warmsg_captcha=(By.XPATH,"//div[@class='ng-star-inserted']")
    contpage_errmsg_invalid_email=(By.XPATH,"//span[normalize-space()='Enter a valid email id']")
    contpage_errmsg_invalid_phone=(By.XPATH,"//span[normalize-space()='Enter a valid phone number with country code']")

    footer_mailaddress_cnp=(By.XPATH, "//div[@class='row mb-lg-130 mb-md-70 mb-40 lg_flagged_information']//div[1]//div[1]//div[1]//p[2]//a[1]")
    footer_contact_num_link_cnp=(By.XPATH,"//p[@class='mb-0 mt-md-30']//a[@class='text-white fontSize-2_0 font-weight-400 no-anchor'][normalize-space()='+ 41 44 552 96 90']")


