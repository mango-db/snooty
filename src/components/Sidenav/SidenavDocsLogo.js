import React from 'react';
import PropTypes from 'prop-types';
import styled from '@emotion/styled';
import { DOCS_URL } from '../../constants';
import { theme } from '../../theme/docsTheme';

import DocsLogo from '../SVGs/DocsLogo';
import Link from '../Link';

const PaddedDocsLogo = styled(DocsLogo)`
  margin: 0px ${theme.size.medium};
`;

const SidenavDocsLogo = ({ border, ...props }) => {
  return (
    <>
      <Link to={`${DOCS_URL}/`}>
        <PaddedDocsLogo height={20} width={184} {...props} />
      </Link>
      {border}
    </>
  );
};

SidenavDocsLogo.propTypes = {
  border: PropTypes.element,
};

export default SidenavDocsLogo;
