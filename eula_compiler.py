from vanilla import *
from vanilla.dialogs import message, putFile

eula_clauses = {
    'title': 'Ghostlines EULA v0.3\n28 November 2016 by Lukas WinklerPrins',
    '0': 'What This Is',
    'the_agreement': 'This End User License Agreement (the "Agreement," "EULA," "License," or "License Agreement") is a legal agreement that dictates the terms of use of the Font Software and the design of the fonts therein (the "Fonts," or "Product") released through the Ghostlines software and platform between you, the licensee (the "User," "End User," or "Licensee"), the designer (the "Foundry," or "Owner"), and Ghostlines.',
    'nonexclusive': 'This EULA is a non-exclusive, non-transferable license for the Font Software which can be revoked.',
    'agreement': 'By downloading the Font Software you agree to this License Agreement and acknowledge that you understand and will comply to the terms stated herein. If you do not accept the terms, you may not download, request, or otherwise use the Fonts.',
    'rights_of_use': 'In agreeing to this License Agreement, you assume the rights to use the Font Software under a specific set of conditions, detailed in section 3.',
    'nondisclosure': 'It is understood and agreed that the Font Software that accompanies this Agreement is and must be kept confidential. You agree not to disclose any information unless required to do so by law.',
    '1': 'Definitions',
    'definition_of_font_software': 'The "Font Software" refers to any whole or partial representation of a font in analog or digital form. This includes the typeface as a whole, as well as individual glyphs. Included in this definition are visual representations of the font software as well as underlying code.',
    'definition_of_user': 'You, the "User," are a recipient of the Font Software through the Ghostlines platform and have been granted limited use rights over the Font Software.',
    'definition_of_designer': 'The Designer is the individual or institution with full ownership and use rights over the Font Software.',
    'definition_of_install': '{definition_of_install}',
    '2': 'Rights of the Designer',
    'designer_owns_rights': 'You (the "User") agree that the designer owns all rights, including (without limitation) intellectual property rights to the Fonts and all trademarks which may be used registered or unregistered in relation to the Fonts.',
    'requirement_to_delete': 'By request of the Designer you must delete all or some copies of the Font Software.',
    'right_to_legal_action': 'The Designer reserves the right to take legal action against any infraction for damages, as well as terminate this use license under any circumstances without notice.',
    'disclaimer': 'DISCLAIMER: GHOSTLINES AND THE DESIGNER ASSUME NO RESPONSIBILITY FOR THE PERFORMANCE OF THE FONTS. THE FONT SOFTWARE IS PROVIDED "AS-IS" WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED. IN NO EVENT SHALL GHOSTLINES OR THE DESIGNER BE HELD LIABLE FOR ANY CLAIM, DAMAGES, OR OTHER LIABILITY ARISING FROM OR OUT OF USE OF THE FONT SOFTWARE.',
    'role_of_ghostlines': 'Ghostlines acts solely as a platform between the User and Designer only and holds no rights to the Font Software or the use of the Font Software sent using its software.',
    '3': 'Rights of the User',
    'limited_permissions': 'You, the Licensee, are allowed to install and use the Font Software in contexts under and limited to your control. You agree to use the Font Software only for local, personal use and examination.',
    'public_use': "The Fonts are intended for feedback and testing use only, and {public_use} be used in public work, commercial or otherwise, up to the Designer's discretion.",
    'number_of_installs': 'The User is allowed {number_of_installs} installation(s) of the Font Software, where each installation follows the terms set in clause 1.4 of this Agreement.',
    'dont_share_it': 'You may not share, distribute, or sell the Font Software as a whole or in parts. You may not package the Fonts with other software that is shared, distributed, or sold.',
    'dont_modify_it': 'You may not to modify, rename, adapt, translate, reverse-engineer, alter, or produce direct derivative work of the Font Software. ',
    'user_backups': 'You may keep additional, uninstalled copies of the Font Software exclusively for the purposes of backing up the files. Unauthorized use of these backup files through sharing or use terminates this license.',
    'crediting_required': 'In all cases of public use, the Designer must be visibly credited for the authorship of the Font Software.',
    'approved_media': '{approved_media}',
    'group_licensing': '{group_licensing}',
    '4': 'Termination and Disputes',
    'termination': 'This Agreement may be terminated by the Designer without notice at any time regardless of circumstance.',
    'user_breach': 'This Agreement terminates in the event that you or any non-authorized user breaches the use terms set forth.',
    'ghostlines_update_termination': 'This Agreement terminates upon update of the Font Software through the Ghostlines platform.',
    'jurisdiction': 'Any dispute regarding the terms of this agreement or its validity, performance, or interpretation shall be subject to the exclusive jurisdiction of the courts of {jurisdiction}.',
    'governing_law': 'This Agreement is governed by and shall be construed in accordance with the laws of {governing_law}.',
    '5': 'Miscellaneous',
    'unenforceable':'If any part of this agreement is found void and unenforceable, it will not affect the validity of the balance of the agreement, which shall remain valid and enforceable according to its terms.',
    'right_to_update_license':'The Designer reserves the right to update this license at any time without notice.',
    'custom_clause': '{custom_clause}',
    'finale': 'Thank you for reading and complying to this agreement!\nFor any inquiries, please get in contact:\n\nGhostlines info@ghostlines.pm'
}

eula_sections = [
    ('0','the_agreement','nonexclusive','agreement','rights_of_use','nondisclosure'),
    ('1','definition_of_font_software','definition_of_user','definition_of_designer','definition_of_install'),
    ('2','designer_owns_rights','requriement_to_delete','right_to_legal_action','disclaimer','role_of_ghostlines'),
    ('3','limited_permissions','public_use','number_of_installs','dont_share_it','dont_modify_it','user_backups','crediting_required','approved_media','group_licensing'),
    ('4','termination','user_breach','ghostlines_update_termination','jurisdiction','governing_law'),
    ('5','unenforceable','right_to_update_license','custom_clause')
]


class EULAGenerator(object):
    def __init__(self):
        self.window = Window((400, 630), "EULA Generator", minSize=(400,300), maxSize=(600,650))
        # [0.5] Nondisclosure checkbox
        self.window.nondisclosure_label = TextBox((40, 10, -10, 17), "Include Nondisclosure Clause?")
        self.window.nondisclosure = CheckBox((10,10,22,22), "",value=False)
        # [1.4] Defining what an 'install' means
        self.window.definition_of_install_label = TextBox((10, 40, -10, 17), "How do you define one font installation?")
        self.window.definition_of_install = TextEditor((10,60,-10,40),'')
        # [3.2] Whether public showing is OK checkbox
        self.window.public_use_label = TextBox((40, 110, -10, 17), "Can your released font be used publicly?")
        self.window.public_use = CheckBox((10,110,22,22), "",value=False)
        # [3.3] Number of installs counter
        self.window.number_of_installs_label = TextBox((70, 150, -10, 17), "Number of installations you allow.")
        self.window.number_of_installs = PopUpButton((10,150,50,21),["1","2","3","4","5+"])
        self.window.number_of_installs.set(0)
        # [3.x] Group Licensing
        self.window.group_licensing_label = TextBox((10, 190, -10, 17), "Do you allow group licensing? How?")
        self.window.group_licensing = TextEditor((10,210,-10,40),"")
        # [3.x] User-made backups checkbox
        self.window.user_backups_label = TextBox((40, 270, -10, 17), "Can the user make archival backups of the font?")
        self.window.user_backups = CheckBox((10,270,22,22), "",value=False)
        # [3.x] Crediting required checkbox
        self.window.crediting_required_label = TextBox((40, 320, -10, 17), "Is the user required to include attribution when sharing?")
        self.window.crediting_required = CheckBox((10,320,22,22), "",value=False)
        # [3.x] Approved Media for Use
        self.window.approved_media_label = TextBox((10, 360, -10, 17), "In what media formats can the user implement the font? (print, web, logos, etc...)")
        self.window.approved_media = TextEditor((10,380,-10,40),"")
        # [4.4] Jurisdiction
        self.window.jurisdiction_label = TextBox((10, 430, -10, 17), "Territory of Jurisdiction (What courts have power?)")
        self.window.jurisdiction = EditText((10,450,-10,22),'e.g. "Los Angeles County"')
        # [4.5] Governing Law
        self.window.governing_law_label = TextBox((10, 480, -10, 17), "Governing Law (Which country's laws apply?)")
        self.window.governing_law = EditText((10,500,-10,22),'e.g. "United States"')
        # [5.x] Write Your Own Clause(s?)
        self.window.custom_clause_label = TextBox((10, 530, -10, 17), "Write Your Own Clause")
        self.window.custom_clause = TextEditor((10,550,-10,40),"")
        # Button to compile and write the EULA.
        self.window.generate_button = Button((10, 600, -10, 20), "Write EULA", self.eula_generate)

    def eula_generate(self, sender):
        user_eula_choices = {
            'definition_of_install': self.window.definition_of_install.get(),
            'public_use': self.window.public_use.get() and 'may' or 'may not',
            'number_of_installs': self.window.number_of_installs.get(),
            'user_backups': self.window.user_backups.get() or '',
            'crediting_required': self.window.crediting_required.get() or '',
            'group_licensing': self.window.group_licensing.get(),
            'approved_media': self.window.approved_media.get(),
            'jurisdiction': self.window.jurisdiction.get(),
            'governing_law': self.window.governing_law.get(),
            'custom_clause': self.window.custom_clause.get(),
        }
        
        user_eula_clauses = dict(eula_clauses)
        for eula_option in user_eula_choices:
            if user_eula_clauses.has_key(eula_option) and user_eula_choices[eula_option]=='':
                del user_eula_clauses[eula_option]
        
        big_eula_array = [user_eula_clauses['title']]
        section_n = 0
        for section in eula_sections:
            clause_n = 0
            for clause in section:
                if user_eula_clauses.has_key(clause):
                    clause_string = "{}.{} {}".format(section_n, clause_n, user_eula_clauses[clause])
                    clause_string = clause_string.format(**user_eula_choices) # not sure why needs to be separated...
                    big_eula_array.append(clause_string)
                    clause_n += 1
            section_n += 1
        big_eula_array.append(user_eula_clauses['finale'])
        print '\n\n'.join(big_eula_array)
        eula_filepath = putFile(fileTypes=['txt'])
        if eula_filepath is not None:
            with open(eula_filepath,'w') as f:
                f.write('\n\n'.join(big_eula_array))
    
    def open(self):
        self.window.open()

EULAGenerator().open()
