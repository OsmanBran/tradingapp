import Box from '@mui/material/Box';
import Card from '@mui/material/Card';
import Stack from '@mui/material/Stack';
import Typography from '@mui/material/Typography';
// ----------------------------------------------------------------------

export default function AppWidgetSummary({ title, total, icon, sx, ...other }: {title: string, total: string, icon?: any, sx?: any, other?: any}) {
  return (
    <Card
      component={Stack}
      spacing={3}
      direction="row"
      sx={{
        px: 3,
        py: 5,
        borderRadius: 2,display: 'flex', justifyContent: 'center',
        ...sx,
      }}
      {...other}
    >
      {icon && <Box sx={{ width: 64, height: 64 }}>{icon}</Box>}

      <Stack spacing={0.5} sx={{display: 'flex', justifyContent: 'center'}}>
        <Typography variant="h4">{total}</Typography>

        <Typography variant="subtitle2" sx={{ color: 'text.disabled' }}>
          {title}
        </Typography>
      </Stack>
    </Card>
  );
}